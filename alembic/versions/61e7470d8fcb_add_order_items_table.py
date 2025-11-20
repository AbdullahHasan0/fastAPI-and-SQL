"""add order_items table

Revision ID: 61e7470d8fcb
Revises: 8752b71672a6
Create Date: 2025-11-20 12:38:48.832484
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers
revision: str = '61e7470d8fcb'
down_revision: Union[str, Sequence[str], None] = '8752b71672a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    # ---------------------------------------------------------------------
    # CREATE TABLE order_items (SQLite-safe)
    # ---------------------------------------------------------------------
    op.execute("""
    CREATE TABLE IF NOT EXISTS order_items (
        id INTEGER PRIMARY KEY,
        order_id INTEGER NOT NULL REFERENCES orders(id),
        product_id INTEGER NOT NULL REFERENCES products(id),
        quantity INTEGER NOT NULL DEFAULT 1,
        unit_price FLOAT NOT NULL DEFAULT 0.0
    )
    """)

    # Create index (only if not exists)
    op.execute("""
    CREATE INDEX IF NOT EXISTS ix_order_items_id
    ON order_items (id)
    """)

    with op.batch_alter_table("products") as batch_op:
        batch_op.alter_column(
            'price',
            existing_type=sa.Integer(),
            type_=sa.Float(),
            existing_nullable=False,
        )


def downgrade() -> None:
    """Downgrade schema."""

    # Drop index if exists
    op.execute("DROP INDEX IF EXISTS ix_order_items_id")

    # Drop table if exists
    op.execute("DROP TABLE IF EXISTS order_items")

    # Revert price column type
    with op.batch_alter_table("products") as batch_op:
        batch_op.alter_column(
            'price',
            existing_type=sa.Float(),
            type_=sa.Integer(),
            existing_nullable=False,
        )
