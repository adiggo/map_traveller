"""add place table

Revision ID: 9d29117b2fc
Revises: 18b529fbbfb
Create Date: 2015-06-03 22:17:28.393854

"""

# revision identifiers, used by Alembic.
revision = '9d29117b2fc'
down_revision = '18b529fbbfb'

from alembic import op
import sqlalchemy as sa
from sqlalchemy import *

def upgrade():
    op.create_table(
      'places',
      Column('id', BigInteger, primary_key=True),
      Column('city', String(length = 200), nullable=False),
      Column('state', String(length = 200), nullable = False),
      Column('country', String(length = 200), nullable = False),
      Column('continent', String(length = 200), nullable = False)
    )

def downgrade():
    op.drop_table('places')
