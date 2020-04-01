from datetime import datetime
from slugify import slugify

from app.models import Entry


MAX_HEADER_LEN = 20
MAX_SIGNATURE_LEN = 10
MAX_BODY_LEN = 1000


def generate_unique_slug(header):
    now = datetime.now()
    publication_date = now.strftime('%Y-%m-%d')
    slug = slugify('{}-{}-0'.format(
        header, publication_date), max_length=32
    )
    entry = Entry.query.get(slug)
    if entry:
        entry_slug = entry.slug
        entry_slug_version = int(entry_slug.split('-')[-1])
        new_version = entry_slug_version + 1
        offset = len(entry_slug) - len(str(entry_slug_version))
        entry_slug_trimmed = entry_slug[:offset]
        new_slug = '{}-{}'.format(entry_slug_trimmed, new_version)
        return new_slug
    return slug


def get_errors(header, signature, body):
    errors = dict()
    if not header:
        errors['header'] = 'Header can\'t be empty'.format(
            MAX_HEADER_LEN
        )
    if len(header) > MAX_HEADER_LEN:
        errors['header'] = 'Header length exceeds {} symbols'.format(
            MAX_HEADER_LEN
        )
    if len(signature) > MAX_SIGNATURE_LEN:
        errors['signature'] = 'Signature length exceeds {} symbols'.format(
            MAX_SIGNATURE_LEN
        )
    if len(body) > MAX_BODY_LEN:
        errors['body'] = 'Body length exceeds {} symbols'.format(
            MAX_BODY_LEN
        )
    return errors
