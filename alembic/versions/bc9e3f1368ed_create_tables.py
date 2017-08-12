"""create tables

Revision ID: bc9e3f1368ed
Revises: 
Create Date: 2017-08-10 21:36:39.613511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc9e3f1368ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("user_id", sa.Integer, primary_key=True, autoincrement=True),    
        sa.Column("user_name", sa.String(32), unique=True),
        sa.Column("user_email", sa.String(32), unique=True),
    )

    op.create_table(
        "programs",
        sa.Column("program_id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("program_name", sa.String(128), unique=True),
    )

    op.create_table(
        "program_enrollments",
        sa.Column("program_enrollment_id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("program_id", sa.Integer, sa.ForeignKey("programs.program_id")),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.user_id")),
    )

def downgrade():
    op.drop_table("users")
    op.drop_table("programs")
    op.drop_table("program_enrollments")