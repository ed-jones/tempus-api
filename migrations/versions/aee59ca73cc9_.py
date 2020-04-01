"""empty message

Revision ID: aee59ca73cc9
Revises: 44b5de0c2b5c
Create Date: 2020-04-01 18:40:56.325034

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'aee59ca73cc9'
down_revision = '44b5de0c2b5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('TOUR_IMAGE',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tour_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('title', sa.String(length=32), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('image', sa.LargeBinary(), nullable=False),
    sa.Column('primary', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['tour_id'], ['TOUR.uuid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('TOUR_IMAGE')
    # ### end Alembic commands ###
