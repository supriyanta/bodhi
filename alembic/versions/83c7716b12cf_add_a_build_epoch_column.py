"""Add a Build.epoch column

Revision ID: 83c7716b12cf
Revises: 6383ec38980
Create Date: 2016-03-01 19:05:54.649231

"""

# revision identifiers, used by Alembic.
revision = '83c7716b12cf'
down_revision = '6383ec38980'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('builds', sa.Column('epoch', sa.Integer, default=0))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('builds', 'epoch')
    ### end Alembic commands ###