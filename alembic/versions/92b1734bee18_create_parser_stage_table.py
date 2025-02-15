"""create parser_stage table

Revision ID: 92b1734bee18
Revises: 05577f7a0d74
Create Date: 2025-02-15 17:35:48.656795

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '92b1734bee18'
down_revision: Union[str, None] = '05577f7a0d74'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create parser_stage table"""
    op.create_table(
        'parser_stage',
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True, comment='Primary key'),
        sa.Column('parsed_date', sa.Date, nullable=False, comment='The date of the parsed dataset (e.g., 2023-01-01)'),
        sa.Column('file_path', sa.String(255), nullable=False, comment='Path to the stored JSON file'),
        sa.Column(
            'status',
            sa.Enum('pending', 'running', 'completed', 'failed', name='status_enum'),
            nullable=False,
            server_default='pending',
            comment='Parsing status'
        ),
        sa.Column('created_at', sa.TIMESTAMP, server_default=sa.func.now(), nullable=True, comment='Record creation timestamp'),
        sa.Column('updated_at', sa.TIMESTAMP, server_default=sa.func.now(), onupdate=sa.func.now(), nullable=True, comment='Record update timestamp'),
    )
    
    # Create indexes
    op.create_index('idx_parsed_date', 'parser_stage', ['parsed_date'])
    op.create_index('idx_file_path', 'parser_stage', ['file_path'])
    op.create_index('idx_status', 'parser_stage', ['status'])
    op.create_index('idx_created_at', 'parser_stage', ['created_at'])
    op.create_index('idx_updated_at', 'parser_stage', ['updated_at'])


def downgrade() -> None:
    """Drop parser_stage table"""
    op.drop_index('idx_updated_at', table_name='parser_stage')
    op.drop_index('idx_created_at', table_name='parser_stage')
    op.drop_index('idx_status', table_name='parser_stage')
    op.drop_index('idx_file_path', table_name='parser_stage')
    op.drop_index('idx_parsed_date', table_name='parser_stage')
    op.drop_table('parser_stage')
