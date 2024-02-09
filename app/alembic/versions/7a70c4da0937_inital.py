"""inital

Revision ID: 7a70c4da0937
Revises: 
Create Date: 2024-02-08 20:38:59.932751

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a70c4da0937'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
            "friend",
            sa.Column("id", sa.String, primary_key=True),
            sa.Column("original_user_id", sa.Integer),
            sa.Column("social_network", sa.String(30)),
            sa.Column("first_name", sa.String(50)),
            sa.Column("last_name", sa.String(50)),
            sa.Column("about", sa.String(500)),
            sa.Column("bdate", sa.String(50)),
            )


def downgrade() -> None:
    op.drop_table("friend")
