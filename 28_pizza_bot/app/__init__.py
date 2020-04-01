import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemyUserDatastore, Security, utils
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from appconfig import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECURITY_PASSWORD_HASH'] = os.getenv(
    'SECURITY_PASSWORD_HASH', 'pbkdf2_sha512'
)
app.config['SECURITY_PASSWORD_SALT'] = os.getenv(
    'SECURITY_PASSWORD_SALT', 'salty'
)
app.config['SECURITY_POST_LOGIN_VIEW'] = '/admin'
app.config['SECURITY_POST_LOGOUT_VIEW'] = '/login'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
from app.orm_models import User, Role, Pizza, Choice


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


# Only needed on first execution to create first user
@app.before_first_request
def create_user():
    db.create_all()
    user_datastore.find_or_create_role(
        name='admin', description='Administrator'
    )
    pizza_admin_email = os.getenv(
        'PIZZA_ADMIN_EMAIL', 'admin@apple.com'
    )
    pizza_admin_password = os.getenv('PIZZA_ADMIN_PASSWORD', '123')
    hashed_password = utils.hash_password(pizza_admin_password)
    if not user_datastore.get_user(pizza_admin_email):
        user_datastore.create_user(
            email=pizza_admin_email,
            password=hashed_password
        )
    db.session.commit()
    user_datastore.add_role_to_user(pizza_admin_email, 'admin')
    db.session.commit()


admin = Admin(
    app, name='Pizza bot admin',
    template_mode='bootstrap3',
    index_view=routes.MyAdminIndexView()
)

admin.add_view(ModelView(orm_models.Pizza, db.session))
admin.add_view(ModelView(orm_models.Choice, db.session))
