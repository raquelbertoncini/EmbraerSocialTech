"""empty message

Revision ID: 389bf33acddd
Revises: 
Create Date: 2022-12-27 12:09:19.650314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '389bf33acddd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('age', sa.String(length=30), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###