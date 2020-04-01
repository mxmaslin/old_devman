"""create orders table

Revision ID: a276037e05ed
Revises: 
Create Date: 2019-04-23 13:18:17.762058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a276037e05ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'orders',
        sa.Column('normalized_phone', sa.String(100), nullable=True)
    )


def downgrade():
    op.drop_column('orders', 'normalized_phone')
