"""create pdfs table

Revision ID: 175d6da57888
Revises: 2bd5421e28e8
Create Date: 2025-07-20 16:30:57.978075

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '175d6da57888'
down_revision: Union[str, Sequence[str], None] = '2bd5421e28e8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pdfs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('file', sa.Text(), nullable=True),
    sa.Column('selected', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pdfs_id'), 'pdfs', ['id'], unique=False)
    op.drop_table('todos')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('completed', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('todos_pkey'))
    )
    op.drop_index(op.f('ix_pdfs_id'), table_name='pdfs')
    op.drop_table('pdfs')
    # ### end Alembic commands ###
