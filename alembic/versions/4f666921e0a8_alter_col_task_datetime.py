"""alter col task_datetime

Revision ID: 4f666921e0a8
Revises: 9db01df362f8
Create Date: 2023-09-16 21:49:21.595151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f666921e0a8'
down_revision = '9db01df362f8'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('to_do_list', 'task_datetime',nullable=False)


def downgrade():
    pass
