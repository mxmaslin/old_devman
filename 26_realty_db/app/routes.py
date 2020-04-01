from flask import render_template, request
from flask_paginate import Pagination, get_page_args

from werkzeug.datastructures import TypeConversionDict

from app import app
from app.models import Flat, Location

MAJOR_LOCATIONS = (("Череповецкий район", "Череповец"),
                   ("Шекснинский район", "Шексна"),
                   ("Вологодский район", "Вологда")
                   )

LOCATIONS = (("Б", (("Бабаевский район", "Бабаево"),
                    ("Бабушкинский район", "Село имени Бабушкина"),
                    ("Белозерский район", "Белозерск")
                    )
              ),
             ("В", (("Великоустюгский район", "Великий Устюг"),
                    ("Верховажский район", "Верховажье"),
                    ("Вожегодский район", "Вожега"),
                    ("Вологодский район", "Вологда"),
                    ("Вытегорский район", "Вытегра")
                    )
              ),
             ("Г", (("Грязовецкий район", "Грязовец"),)),
             ("К", (("Кадуйский район", "Кадуй"),
                    ("Кирилловский район", "Кириллов"),
                    ("Кичменгско-Городецкий район", "Кичменгский Городок"))
              ),
             ("Л", (("Вашкинский район", "Липин"),)),
             ("Н", (("Никольский район", "Никольск"),
                    ("Нюксенский район", "Нюксеница"))
              ),
             ("С", (("Сокольский район", "Сокол"),
                    ("Сямженский район", "Сямжа")
                    )
              ),
             ("Т", (("Тарногский район", "Тарногский"),
                    ("Тотемский район", "Тотьма"))
              ),
             ("У", (("Усть-Кубинский район", "Устье"),
                    ("Устюженский район", "Устюжна"))
              ),
             ("Х", (("Харовский район", "Харовск"),)
              ),
             ("Ч", (("Чагодощенский район", "Чагода"),
                    ("Череповецкий район", "Череповец")
                    )
              ),
             ("Ш", (("Шекснинский район", "Шексна"),
                    ("Междуреченский район", "Шуйское")
                    )
              )
             )

MIN_PRICE = 0
MAX_PRICE = 10000000


def get_flats(flats, offset=0, per_page=app.config['ADS_PER_PAGE']):
    return flats[offset: offset + per_page]


@app.route('/')
def ads_list():
    oblast_district = request.args.get('oblast_district')
    type_conversion_dict = TypeConversionDict(
        under_construction=request.args.get('min_price') or MIN_PRICE
    )
    min_price = type_conversion_dict.get(
        'under_construction', type=int
    )
    type_conversion_dict = TypeConversionDict(
        under_construction=request.args.get('max_price') or MAX_PRICE
    )
    max_price = type_conversion_dict.get(
        'under_construction', type=int
    )
    type_conversion_dict = TypeConversionDict(
        under_construction=request.args.get('new_building')
    )
    under_construction = type_conversion_dict.get(
        'under_construction', type=bool
    )

    flats = Flat.query.join(Location).filter(
        Location.oblast_district == oblast_district,
        Flat.price >= min_price,
        Flat.price <= max_price,
        Flat.under_construction.is_(under_construction),
        Flat.is_active.is_(True)
    ).order_by(Flat.price.asc())

    if not any([
        oblast_district, min_price != MIN_PRICE, max_price != MAX_PRICE
    ]):
        flats = Flat.query.order_by(Flat.price.asc())

    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page'
    )
    pagination_flats = get_flats(flats, offset=offset, per_page=per_page)
    pagination = Pagination(
        page=page,
        per_page=per_page,
        total=flats.count()
    )

    return render_template(
        'ads_list.html',
        flats=pagination_flats,
        pagination=pagination,
        page=page,
        per_page=per_page,
        major_locations=MAJOR_LOCATIONS,
        locations=LOCATIONS
    )


if __name__ == "__main__":
    app.run()
