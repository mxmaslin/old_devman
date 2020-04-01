from flask import render_template
from flask_admin import AdminIndexView
from flask_security import current_user, login_required

from app import app
from app.orm_models import Pizza


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.has_role('admin')


@app.route('/')
@login_required
def index():
    pizzas = Pizza.query.all()
    return render_template('index.html', pizzas=pizzas)
