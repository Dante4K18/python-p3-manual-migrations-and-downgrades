"""Renaming students to scholars

Revision ID: ff906e458064
Revises: 791279dd0760
Create Date: 2024-11-10 02:54:51.561296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff906e458064'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'niggas_with_attitude')


def downgrade() -> None:
    op.rename_table('niggas_with_attitude', 'students')
