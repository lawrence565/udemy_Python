"""Create an address table

Revision ID: 8b66dc325d1f
Revises: 
Create Date: 2024-09-24 16:25:31.516598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b66dc325d1f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('address', 
	sa.Column('id', sa.Integer, primary_key=True), 
	sa.Column('address', sa.String(50), nullable=False), 
	sa.Column('city', sa.String(50), nullable=False),
	sa.Column('State', sa.String(50), nullable=False)
	)


def downgrade():
    op.drop_table('address')
