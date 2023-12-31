"""comment

Revision ID: eb349ed955a4
Revises: a910f59a9b63
Create Date: 2023-01-05 19:07:29.625130

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'eb349ed955a4'
down_revision = 'a910f59a9b63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('title', mysql.VARCHAR(length=255), nullable=True))
    # ### end Alembic commands ###
