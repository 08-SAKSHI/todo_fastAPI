"""todo_table

Revision ID: bfbceb41a35f
Revises: 
Create Date: 2023-09-16 20:48:37.176434

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql as ms


# revision identifiers, used by Alembic.
revision = 'bfbceb41a35f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "to_do_list",
        sa.Column("task_id", ms.BIGINT(19), nullable=False),
        sa.Column("task_title", ms.VARCHAR(200), nullable=False),
        sa.Column("task_datetime",ms.DATETIME,nullable=True),
        sa.Column("task_status", ms.BOOLEAN(), nullable=True),
        sa.PrimaryKeyConstraint("task_id")
    )


def downgrade():
    op.drop_table("to_do_list")

