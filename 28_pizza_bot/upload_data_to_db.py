import json

from fixtures import catalog
from app import db
from app.orm_models import Choice, Pizza


if __name__ == '__main__':
    for entry in catalog:
        choices = [Choice(title=x['title'], price=x['price'])
                   for x in entry['choices']
                   ]
        pizza = Pizza(title=entry['title'], description=entry['description'])
        pizza.choices.extend(choices)
        db.session.add(pizza)
        db.session.add_all(choices)
        db.session.commit()
