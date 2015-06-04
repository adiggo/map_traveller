"""add user_places table

Revision ID: 276102e0be8b
Revises: 9d29117b2fc
Create Date: 2015-06-03 22:19:28.290975

"""

# revision identifiers, used by Alembic.
revision = '276102e0be8b'
down_revision = '9d29117b2fc'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy import *

def upgrade():
    op.create_table(
      'user_places',
      Column('id', BigInteger, primary_key = True),
      Column('user_id', BigInteger, ForeignKey('users.id', name='fk_user_places_user_id'), nullable = False),
      Column('place_id', BigInteger, ForeignKey('places.id', name='fk_user_places_place_id'), nullable = False),
      Column('started_at', DateTime, nullable = False),
      Column('left_at', DateTime, nullable = False)
    )


def downgrade():
    op.drop_table('user_places')
