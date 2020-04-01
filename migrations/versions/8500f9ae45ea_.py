"""empty message

Revision ID: 8500f9ae45ea
Revises: 699a48d800f1
Create Date: 2020-03-30 17:44:34.296236

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8500f9ae45ea'
down_revision = '699a48d800f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('TOUR_DATE',
    sa.Column('id', sa.Integer(), server_default=FetchedValue(), nullable=False),
    sa.Column('tour_id', sa.Integer(), nullable=True),
    sa.Column('tour_date', sa.DateTime(), server_default=FetchedValue(), nullable=True),
    sa.ForeignKeyConstraint(['tour_id'], ['TOUR.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('LANGUAGE_pkey', table_name='LANGUAGE')
    op.alter_column('TOUR', 'duration',
               existing_type=postgresql.INTERVAL(),
               nullable=True)
    op.alter_column('TOUR', 'guide_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('TOUR', 'price',
               existing_type=sa.REAL(),
               nullable=True)
    op.alter_column('TOUR', 'rating',
               existing_type=sa.REAL(),
               nullable=True)
    op.alter_column('TOUR', 'title',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    op.alter_column('TOUR', 'upload_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True,
               existing_server_default=sa.text('now()'))
    op.create_unique_constraint(None, 'TOUR', ['uuid'])
    op.alter_column('USER', 'password',
               existing_type=sa.VARCHAR(length=60),
               nullable=False)
    op.create_unique_constraint(None, 'USER', ['uuid'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'USER', type_='unique')
    op.alter_column('USER', 'password',
               existing_type=sa.VARCHAR(length=60),
               nullable=True)
    op.drop_constraint(None, 'TOUR', type_='unique')
    op.alter_column('TOUR', 'upload_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('now()'))
    op.alter_column('TOUR', 'title',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    op.alter_column('TOUR', 'rating',
               existing_type=sa.REAL(),
               nullable=False)
    op.alter_column('TOUR', 'price',
               existing_type=sa.REAL(),
               nullable=False)
    op.alter_column('TOUR', 'guide_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('TOUR', 'duration',
               existing_type=postgresql.INTERVAL(),
               nullable=False)
    op.create_index('LANGUAGE_pkey', 'LANGUAGE', ['id'], unique=True)
    op.drop_table('TOUR_DATE')
    # ### end Alembic commands ###
