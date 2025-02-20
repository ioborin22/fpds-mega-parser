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

# sa.Column('###', sa.String(255), nullable=True, index=True, comment=""),
def upgrade():
    """Create contracts table."""
    op.create_table(
        'contracts',
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True, comment="Primary key"),
        # Тип контракта (например, AWARD, IDV, OTHERTRANSACTIONAWARD, OTHERTRANSACTIONIDV).
        sa.Column('contract_type', sa.String(255), nullable=True, index=True, comment="The type of contract (e.g., IDV, AWARD, OTHERTRANSACTIONAWARD)"),
        # Дата и время последнего изменения данных о контракте.
        sa.Column('modified', sa.TIMESTAMP, nullable=True, comment=""),
        # Код агентства, заключившего контракт.
        sa.Column('agency_id', sa.String(255), nullable=True, index=True, comment=""),
        # Уникальный идентификатор контракта (Procurement Instrument Identifier, PIID).
        sa.Column('piid', sa.String(255), nullable=True, comment="The Procurement Instrument Identifier (PIID)"),
        # Номер модификации контракта.
        sa.Column('mod_number', sa.String(255), nullable=True, comment="The modification number of the award or contract"),
        # IDV
        sa.Column('idv_piid', sa.String(255), nullable=True, comment="The PIID of the IDV contract if applicable"),
        # PIID для родительского контракта
        sa.Column('referenced_piid', sa.String(255), nullable=True, index=True, comment="The PIID for the referenced award or contract"),
        # Дата подписания контракта.
        sa.Column('signed_date', sa.Date, nullable=True, index=True, comment="The date the contract was signed"),
        # Дата вступления контракта в силу.
        sa.Column('effective_date', sa.Date, nullable=True, index=True, comment="The effective start date of the contract"),
        # Окончательная дата завершения контракта, учитывая все возможные продления.
        sa.Column('ultimate_completion_date', sa.Date, nullable=True, index=True, comment=""),
        # Сумма, фактически выделенная по контракту (обязательства по оплате).
        sa.Column('obligated_amount', sa.Numeric(15, 2), nullable=True, index=True, comment="The obligated amount of funds for the contract"),
        # Полная стоимость контракта, включая все возможные опции (даже если они ещё не активированы).
        sa.Column('base_and_all_options_value', sa.Numeric(15, 2), nullable=True, index=True, comment="The value of base and all options"),
        # Общая сумма, выделенная по контракту (включает все модификации и изменения).
        sa.Column('total_obligated_amount', sa.Numeric(15, 2), nullable=True, index=True, comment=""),
        # Полная стоимость контракта, включая базовую сумму и все возможные опции (даже если они не активированы).
        sa.Column('total_base_and_all_options_value', sa.Numeric(15, 2), nullable=True, index=True, comment=""),
        # Код агентства, заключившего контракт.
        sa.Column('contracting_office_agency_id', sa.String(255), nullable=True, index=True, comment="The ID of the contracting office agency"),
        # Код контрактного офиса, который оформил контракт.
        sa.Column('contracting_office_id', sa.String(255), nullable=True, index=True, comment="The ID of the contracting office"),
        # Код агентства, запрашивающего финансирование для контракта.
        sa.Column('funding_requesting_agency_id', sa.String(255), nullable=True, index=True, comment="The ID of the funding or requesting agency"),
        # Код офиса, запрашивающего финансирование для контракта.
        sa.Column('funding_requesting_office_id', sa.String(255), nullable=True, index=True, comment="The ID of the funding or requesting office"),
        # Описание типа действия по контракту.
        sa.Column('contract_action_type_description', sa.String(255), nullable=True, index=True, comment=""),
        # Тип ценообразования.
        sa.Column('type_of_contract_pricing_description', sa.String(255), nullable=True, index=True, comment=""),
        # Описание требований к контракту – цель и предмет закупки.
        sa.Column('description_of_contract_requirement', sa.String(255), nullable=True, index=True, comment=""),
        # Указывает, является ли контракт многолетним.
        sa.Column('multi_year_contract', sa.String(255), nullable=True, index=True, comment=""),
        # Указывает, является ли связанный IDV (Indefinite Delivery Vehicle) контрактом с одним или несколькими поставщиками.
        sa.Column('referenced_idv_multiple_or_single', sa.String(255), nullable=True, index=True, comment=""),
        # Указывает тип IDV-контракта (Indefinite Delivery Vehicle).
        sa.Column('referenced_idv_type', sa.String(255), nullable=True, index=True, comment=""),
        # Указывает, применяются ли к контракту требования по стандартам труда.
        sa.Column('labor_standards', sa.String(255), nullable=True, index=True, comment=""),
        # Код, обозначающий тип продукции или услуги, предоставляемой по контракту.
        sa.Column('psc_code', sa.String(255), nullable=True, index=True, comment="The product or service code"),
        # Определяет, относится ли контракт к категории "товары" (Product) или "услуги" (Service).
        sa.Column('psc_type', sa.String(255), nullable=True, index=True, comment=""),
        # Основной код отрасли по системе NAICS (North American Industry Classification System).
        sa.Column('naics_code', sa.String(255), nullable=True, index=True, comment="The principal NAICS code"),
        # Код страны происхождения товара или услуги.
        sa.Column('country_of_origin', sa.String(255), nullable=True, index=True, comment=""),
        # Официальное название поставщика, заключившего контракт.
        sa.Column('vendor_name', sa.String(255), nullable=True, index=True, comment=""),
        # Указывает, относится ли компания к категории малого бизнеса.
        sa.Column('is_small_business', sa.Boolean(), nullable=True, index=True, comment=""),
        # Указывает, принадлежит ли компания ветерану с ограниченными возможностями, связанными со службой.
        sa.Column('is_veteran_owned_business', sa.Boolean(), nullable=True, index=True, comment=""),
        # Указывает, принадлежит ли компания женщине.
        sa.Column('is_women_owned_business', sa.Boolean(), nullable=True, index=True, comment=""),
        # Указывает, является ли компания очень малым бизнесом.
        sa.Column('is_very_small_business', sa.Boolean(), nullable=True, index=True, comment=""),
        # Указывает, принадлежит ли компания малому бизнесу, управляемому женщиной.
        sa.Column('is_women_owned_small_business', sa.Boolean(), nullable=True, index=True, comment=""),
        # Указывает, принадлежит ли компания экономически обездоленной женщине, владеющей малым бизнесом.
        sa.Column('is_economically_disadvantaged_women_owned_small_business', sa.Boolean(), nullable=True, index=True, comment=""),
        # Указывает, является ли организация партнёрством или партнёрством с ограниченной ответственностью.
        sa.Column('is_partnership_or_limited_liability_partnership', sa.Boolean(), nullable=True, index=True, comment=""),
        # Указывает, получает ли организация как контракты, так и гранты от федерального правительства.
        sa.Column('receives_contracts_and_grants', sa.Boolean(), nullable=True, index=True, comment=""),
        # Указывает, является ли организация коммерческой, целью которой является получение прибыли.
        sa.Column('is_for_profit_organization', sa.Boolean(), nullable=True, index=True, comment=""),
        # Указывает штат, в котором зарегистрирована организация.
        sa.Column('vendor_state_of_incorporation', sa.String(255), nullable=True, index=True, comment=""),
        # Указывает страну, в которой зарегистрирована организация.
        sa.Column('vendor_country_of_incorporation', sa.String(255), nullable=True, index=True, comment=""),
        # Город, в котором расположена организация.
        sa.Column('vendor_location_city', sa.String(255), nullable=True, index=True, comment=""),
        # Код штата, в котором расположена организация.
        sa.Column('vendor_location_state', sa.String(255), nullable=True, index=True, comment=""),
        # Почтовый индекс местоположения организации.
        sa.Column('vendor_location_zipcode', sa.String(255), nullable=True, index=True, comment=""),
        # Код страны, в которой расположена организация.
        sa.Column('vendor_location_country', sa.String(255), nullable=True, index=True, comment=""),
        # Уникальный идентификатор организации (UEI), используемый для официальной идентификации.
        sa.Column('vendor_uei', sa.String(255), nullable=True, index=True, comment=""),
        # UEI основного (родительского) бизнеса или организации, которая является владельцем или управляющим.
        sa.Column('vendor_ultimate_parent_uei', sa.String(255), nullable=True, index=True, comment=""),
        # CAGE (Commercial and Government Entity) код, присвоенный организации для государственных контрактов.
        sa.Column('vendor_cage_code', sa.String(255), nullable=True, index=True, comment=""),
        # Дата регистрации организации в CCR.
        sa.Column('vendor_registration_date', sa.Date, nullable=True, index=True, comment=""),
        # Дата продления регистрации организации в CCR.
        sa.Column('vendor_renewal_date', sa.Date, nullable=True, index=True, comment=""),
        # Оценка размера бизнеса, произведённая контрактующим офицером.
        sa.Column('vendor_size', sa.String(255), nullable=True, index=True, comment=""),
        # Код штата, в котором выполняется контракт.
        sa.Column('place_of_performance_state', sa.String(255), nullable=True, index=True, comment=""),
        # Код страны, в которой выполняется контракт.
        sa.Column('place_of_performance_country', sa.String(255), nullable=True, index=True, comment=""),
        # Почтовый индекс места исполнения контракта.
        sa.Column('place_of_performance_zip', sa.String(255), nullable=True, index=True, comment=""),
        # Уровень конкуренции по контракту.
        sa.Column('competition_extent_competed', sa.String(255), nullable=True, index=True, comment=""),
        # Процедура подачи предложений для контракта.
        sa.Column('competition_solicitation_procedures', sa.String(255), nullable=True, index=True, comment=""),
        # Причина, по которой контракт не был конкурентным.
        sa.Column('competition_reason_not_competed', sa.String(255), nullable=True, index=True, comment=""),
        # !!!!!!!
        sa.Column('competition_number_of_offers_received', sa.String(255), nullable=True, index=True, comment=""),
        # Количество предложений, полученных для контракта.
        sa.Column('competition_idv_number_of_offers_received', sa.String(255), nullable=True, index=True, comment=""),
        # Указывает, были ли сделаны публичные объявления о федеральных бизнес-возможностях (Federal Business Opportunities).
        sa.Column('competition_fed_biz_opps', sa.String(255), nullable=True, index=True, comment=""),
        # Статус транзакции.
        sa.Column('award_transaction_information_status', sa.String(255), nullable=True, index=True, comment=""),

        sa.Column('file_path', sa.String(255), nullable=False, comment="The file path to the stored file data"),
        sa.Column('created_at', sa.TIMESTAMP, nullable=True, server_default=sa.text('CURRENT_TIMESTAMP'), comment="Timestamp of record creation"),
        sa.Column('updated_at', sa.TIMESTAMP, nullable=True, server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), comment="Timestamp of last update"),
    )


def downgrade():
    """Drop contracts table."""
    op.drop_table('contracts')