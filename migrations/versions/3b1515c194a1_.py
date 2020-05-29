"""empty message

Revision ID: 3b1515c194a1
Revises: 057e8704e95c
Create Date: 2020-05-29 16:54:18.643370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b1515c194a1'
down_revision = '057e8704e95c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('REVIEW', sa.Column('review_type', sa.Enum('FROM_HOSTS', 'FROM_GUESTS', name='reviewtype'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('REVIEW', 'review_type')
    # ### end Alembic commands ###
