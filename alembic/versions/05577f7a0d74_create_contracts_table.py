"""create contracts table

Revision ID: 05577f7a0d74
Revises: 
Create Date: 2025-02-15 17:35:00.588374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05577f7a0d74'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """Create contracts table."""
    op.create_table(
        'contracts',
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True, comment="Primary key"),
        sa.Column('piid', sa.String(255), nullable=True, comment="The Procurement Instrument Identifier (PIID)"),
        sa.Column('idv_piid', sa.String(255), nullable=True, comment="The PIID of the IDV contract if applicable"),
        sa.Column('referenced_piid', sa.String(255), nullable=True, index=True, comment="The PIID for the referenced award or contract"),
        sa.Column('mod_number', sa.String(255), nullable=True, comment="The modification number of the award or contract"),
        sa.Column('transaction_number', sa.String(255), nullable=True, comment="The transaction number for the award or contract"),
        sa.Column('signed_date', sa.Date, nullable=True, index=True, comment="The date the contract was signed"),
        sa.Column('effective_date', sa.Date, nullable=True, index=True, comment="The effective start date of the contract"),
        sa.Column('current_completion_date', sa.Date, nullable=True, index=True, comment="The current completion date of the contract"),
        sa.Column('obligated_amount', sa.Numeric(15, 2), nullable=True, index=True, comment="The obligated amount of funds for the contract"),
        sa.Column('base_and_exercised_options_value', sa.Numeric(15, 2), nullable=True, index=True, comment="The value of base and exercised options"),
        sa.Column('base_and_all_options_value', sa.Numeric(15, 2), nullable=True, index=True, comment="The value of base and all options"),
        sa.Column('vendor_uei', sa.String(255), nullable=True, index=True, comment="The Unique Entity Identifier (UEI) of the vendor"),
        sa.Column('naics_code', sa.String(255), nullable=True, index=True, comment="The principal NAICS code"),
        sa.Column('psc_code', sa.String(255), nullable=True, index=True, comment="The product or service code"),
        sa.Column('contracting_office_agency_id', sa.String(255), nullable=True, index=True, comment="The ID of the contracting office agency"),
        sa.Column('contracting_office_id', sa.String(255), nullable=True, index=True, comment="The ID of the contracting office"),
        sa.Column('funding_requesting_agency_id', sa.String(255), nullable=True, index=True, comment="The ID of the funding or requesting agency"),
        sa.Column('funding_requesting_office_id', sa.String(255), nullable=True, index=True, comment="The ID of the funding or requesting office"),
        sa.Column('number_of_offers_received', sa.Integer, nullable=True, comment="Number of offers received for the contract"),
        sa.Column('extent_competed', sa.String(255), nullable=True, index=True, comment="Extent of competition for the contract"),
        sa.Column('file_path', sa.String(255), nullable=False, comment="The file path to the stored file data"),
        sa.Column('created_at', sa.TIMESTAMP, nullable=True, server_default=sa.text('CURRENT_TIMESTAMP'), comment="Timestamp of record creation"),
        sa.Column('updated_at', sa.TIMESTAMP, nullable=True, server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), comment="Timestamp of last update"),
    )


def downgrade():
    """Drop contracts table."""
    op.drop_table('contracts')