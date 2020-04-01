from app import db


class Entry(db.Model):
    slug = db.Column(db.String(40), primary_key=True)
    header = db.Column(
        db.String(20),
        index=True,
        nullable=False,
        default='empty-header'
    )
    unique_id = db.Column(db.String(60))
    signature = db.Column(db.String(10), index=True)
    body = db.Column(db.String(1000), index=True)

    def __repr__(self):
        return '<Entry {}>'.format(self.slug)
