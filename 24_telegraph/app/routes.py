import os
import uuid

from flask import (render_template,
                   request,
                   redirect,
                   url_for,
                   send_from_directory,
                   session,
                   abort
                   )

from app import app, db

from app.models import Entry
from app.helpers import generate_unique_slug, get_errors


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(
            app.root_path, 'static'
        ), 'favicon.ico', mimetype='image/vnd.microsoft.icon'
    )


def make_unique_id():
    return uuid.uuid4().hex


@app.route('/<slug>', methods=['GET', 'POST'])
def entry(slug):
    entry = Entry.query.get(slug)
    if not entry:
        error_404 = 404
        abort(error_404)
    header = entry.header
    signature = entry.signature
    body = entry.body
    unique_id = entry.unique_id
    can_edit = False
    errors = dict()
    if 'id' in session and session.get('id') == unique_id:
        can_edit = True
    if request.method == 'POST' and can_edit:
        form_data = request.form
        header = form_data.get('header')
        signature = form_data.get('signature')
        body = form_data.get('body')
        errors = get_errors(header, signature, body)
        if not errors:
            entry = Entry.query.get(slug)
            entry.header = header
            entry.signature = signature
            entry.body = body
            db.session.add(entry)
            db.session.commit()
    context = {
        'can_edit': can_edit,
        'index_page': False,
        'header': {
            'content': header, 'error': errors.get('header')
        },
        'signature': {
            'content': signature, 'error': errors.get('signature')
        },
        'body': {'content': body, 'error': errors.get('body')}}
    return render_template('form.html', context=context)


@app.route('/', methods=['GET', 'POST'])
def form():
    header = None
    signature = None
    body = None
    errors = dict()
    if request.method == 'POST':
        form_data = request.form
        header = form_data.get('header')
        signature = form_data.get('signature')
        body = form_data.get('body')
        errors = get_errors(header, signature, body)
        if not errors:
            slug = generate_unique_slug(header)
            if 'id' in session:
                unique_id = session.get('id')
            else:
                unique_id = make_unique_id()
                session['id'] = unique_id
            entry = Entry(
                slug=slug,
                header=header,
                unique_id=unique_id,
                signature=signature,
                body=body
            )
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for('entry', slug=slug))
    context = {
        'can_edit': True,
        'index_page': True,
        'header': {'content': header, 'error': errors.get('header')},
        'signature': {'content': signature, 'error': errors.get('signature')},
        'body': {'content': body, 'error': errors.get('body')},
        'now': None
    }
    return render_template('form.html', context=context)
