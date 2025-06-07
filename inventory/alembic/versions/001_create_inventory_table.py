"""create inventory table

Revision ID: 001
Revises: 
Create Date: 2025-06-07

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic
revision: str = '001'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'inventory',
        sa.Column('product_id', sa.Integer, primary_key=True, index=True),
        sa.Column('quantity', sa.Integer, index=True),
    )
    op.create_index(op.f('idx_inventory_product_id'), 'inventory', ['product_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('idx_inventory_product_id'), table_name='inventory')
    op.drop_table('inventory')