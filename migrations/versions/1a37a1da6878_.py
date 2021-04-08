"""empty message

Revision ID: 1a37a1da6878
Revises: 338769bb4f87
Create Date: 2021-04-04 14:40:22.658530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a37a1da6878'
down_revision = '338769bb4f87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('updated_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'updated_date')
    # ### end Alembic commands ###
