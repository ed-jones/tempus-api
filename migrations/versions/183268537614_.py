"""empty message

Revision ID: 183268537614
Revises: 8500f9ae45ea
Create Date: 2020-03-30 18:55:11.075231

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '183268537614'
down_revision = '8500f9ae45ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('LANGUAGE',
    sa.Column('id', sa.String(length=5), server_default=FetchedValue(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('USER',
    sa.Column('id', sa.Integer(), server_default=FetchedValue(), nullable=False),
    sa.Column('uuid', postgresql.UUID(as_uuid=True), server_default=FetchedValue(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('firstname', sa.String(length=32), nullable=False),
    sa.Column('lastname', sa.String(length=32), nullable=False),
    sa.Column('customer_rating', sa.Float(), nullable=True),
    sa.Column('guide_rating', sa.Float(), nullable=True),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('TOUR',
    sa.Column('id', sa.Integer(), server_default=FetchedValue(), nullable=False),
    sa.Column('guide_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=32), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('uuid', postgresql.UUID(as_uuid=True), server_default=FetchedValue(), nullable=False),
    sa.Column('upload_time', sa.DateTime(), server_default=FetchedValue(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('duration', sa.Interval(), nullable=True),
    sa.ForeignKeyConstraint(['guide_id'], ['USER.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('VERNACULAR',
    sa.Column('id', sa.Integer(), server_default=FetchedValue(), nullable=False),
    sa.Column('language_id', sa.String(length=5), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['language_id'], ['LANGUAGE.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['USER.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('LOCATION',
    sa.Column('id', sa.Integer(), server_default=FetchedValue(), nullable=False),
    sa.Column('tour_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('address', sa.String(length=60), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lng', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['tour_id'], ['TOUR.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('TOUR_DATE',
    sa.Column('id', sa.Integer(), server_default=FetchedValue(), nullable=False),
    sa.Column('tour_id', sa.Integer(), nullable=True),
    sa.Column('tour_date', sa.DateTime(), server_default=FetchedValue(), nullable=True),
    sa.ForeignKeyConstraint(['tour_id'], ['TOUR.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('TOUR_IMAGE',
    sa.Column('id', sa.Integer(), server_default=FetchedValue(), nullable=False),
    sa.Column('tour_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=32), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('image', sa.LargeBinary(), nullable=True),
    sa.ForeignKeyConstraint(['tour_id'], ['TOUR.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('TOUR_IMAGE')
    op.drop_table('TOUR_DATE')
    op.drop_table('LOCATION')
    op.drop_table('VERNACULAR')
    op.drop_table('TOUR')
    op.drop_table('USER')
    op.drop_table('LANGUAGE')
    # ### end Alembic commands ###
