"""Renaming students to scholars

Revision ID: 3c03eeb035c1
Revises: 2f94ef307f88
Create Date: 2024-09-12 23:09:38.631876

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c03eeb035c1'
down_revision: Union[str, None] = '2f94ef307f88'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
