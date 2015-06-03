"""add user table

Revision ID: 18b529fbbfb
Revises: 
Create Date: 2015-06-02 23:13:56.346905

"""

# revision identifiers, used by Alembic.
revision = '18b529fbbfb'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
from alembic import op
from sqlalchemy import *
from sqlalchemy.dialects.mysql import INTEGER as Integer, VARCHAR


def upgrade():
    op.create_table(
      'users',
      Column('id', Integer(unsigned=True), primary_key=True, nullable=False),
      Column('name', String(length=200), nullable=False),
      Column('email', String(length=200)),
      Column('password', String(length=200)),
      Column('fid', String(length=200)),
      Column('wid', String(length=200)),
      Column('date_of_birth', DateTime),
      Column('profile_photo', String(length=200)),
      Column('created_at', DateTime, nullable=False),
      Column('updated_at', DateTime, nullable=False),
    )


def downgrade():
    op.drop_table('users')
