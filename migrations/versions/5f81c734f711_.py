"""empty message

Revision ID: 5f81c734f711
Revises: 1172debb49f0
Create Date: 2020-05-28 15:04:46.794698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f81c734f711'
down_revision = '1172debb49f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('USER', sa.Column('website', sa.String(length=60), nullable=True))
    op.drop_column('USER', 'url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('USER', sa.Column('url', sa.VARCHAR(length=60), autoincrement=False, nullable=True))
    op.drop_column('USER', 'website')
    # ### end Alembic commands ###
