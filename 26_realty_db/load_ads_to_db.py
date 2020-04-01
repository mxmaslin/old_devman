import json

from app import db
from app.models import Flat, Location

with open('ads.json') as file:
    file_contents = file.read()
    ads = json.loads(file_contents)

for ad in ads:
    location = Location(
        oblast_district=ad.get('oblast_district'),
        settlement=ad.get('settlement'),
        address=ad.get('address')
    )
    flat = Flat(
        under_construction=ad.get('under_construction'),
        description=ad.get('description'),
        price=ad.get('price'),
        living_area=ad.get('living_area'),
        has_balcony=ad.get('has_balcony'),
        construction_year=ad.get('construction_year'),
        rooms_number=ad.get('rooms_number'),
        premise_area=ad.get('premise_area'),
        id=ad.get('id'),
        location_id=location.id,
        location=location,
        is_active=True

    )
    if not Flat.query.filter(Flat.id == flat.id).count():
        db.session.add(location)
        db.session.add(flat)
db.session.commit()

json_flat_ids = [x.get('id') for x in ads]
db_flats = Flat.query.filter(Flat.is_active.is_(True))
mappings = []
for flat in db_flats:
    if flat.id not in json_flat_ids:
        flat.is_active = False
        mappings.append({'id': flat.id, 'is_active': False})
db.session.bulk_update_mappings(Flat, mappings)
db.session.commit()
