"""empty message

Revision ID: 44b5de0c2b5c
Revises: 005c48c4e7f2
Create Date: 2020-04-01 16:17:25.080744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44b5de0c2b5c'
down_revision = '005c48c4e7f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'TOUR', ['uuid'])
    op.add_column('TOUR_IMAGE', sa.Column('primary', sa.Boolean(), server_default='TRUE', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('TOUR_IMAGE', 'primary')
    op.drop_constraint(None, 'TOUR', type_='unique')
    # ### end Alembic commands ###
