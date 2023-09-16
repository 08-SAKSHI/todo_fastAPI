"""alter todo table

Revision ID: 9db01df362f8
Revises: bfbceb41a35f
Create Date: 2023-09-16 21:33:59.120946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9db01df362f8'
down_revision = 'bfbceb41a35f'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('to_do_list', 'task_id',autoincrement=True)

def downgrade():
    pass
