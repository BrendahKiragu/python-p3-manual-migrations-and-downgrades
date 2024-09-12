"""Renaming students to scholars

Revision ID: 2f94ef307f88
Revises: 894aa81a1f2f
Create Date: 2024-09-12 23:06:51.994823

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2f94ef307f88'
down_revision: Union[str, None] = '894aa81a1f2f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
