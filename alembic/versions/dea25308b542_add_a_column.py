"""Add a column

Revision ID: dea25308b542
Revises: bc9e3f1368ed
Create Date: 2017-08-10 21:38:46.721244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dea25308b542'
down_revision = 'bc9e3f1368ed'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "programs",        
        sa.Column("user_id", sa.Integer, primary_key=True, nullable=True),
    )


def downgrade():
    pass

