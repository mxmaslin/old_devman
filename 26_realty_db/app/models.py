from app import db


class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True)
    oblast_district = db.Column(db.String(100), nullable=False, default='', index=True)
    settlement = db.Column(db.String(100), nullable=False, default='')
    address = db.Column(db.String(100), nullable=False, default='')


class Flat(db.Model):
    __tablename__ = 'flat'
    id = db.Column(db.Integer, primary_key=True)
    under_construction = db.Column(db.Boolean, default=False, index=True)
    description = db.Column(db.String(1000), nullable=False, default='')
    price = db.Column(db.Integer, nullable=True, index=True)
    living_area = db.Column(db.Float, nullable=True)
    premise_ares = db.Column(db.Float, nullable=True)
    has_balcony = db.Column(db.Boolean, default=False)
    construction_year = db.Column(db.Integer, nullable=True)
    rooms_number = db.Column(db.Integer)
    premise_area = db.Column(db.Float, nullable=True)
    location_id = db.Column(db.Integer, db.ForeignKey(
        'location.id'), index=True
                            )
    location = db.relationship('Location', backref='location')
    is_active = db.Column(db.Boolean, default=False)
