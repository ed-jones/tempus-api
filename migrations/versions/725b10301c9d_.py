"""empty message

Revision ID: 725b10301c9d
Revises: 3b1515c194a1
Create Date: 2020-05-29 16:56:51.637018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '725b10301c9d'
down_revision = '3b1515c194a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('REVIEW', sa.Column('review_type', sa.Enum('FROM_HOSTS', 'FROM_GUESTS', name='reviewtype'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('REVIEW', 'review_type')
    # ### end Alembic commands ###
