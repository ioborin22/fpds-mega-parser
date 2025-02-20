"title": "New DELIVERY ORDER 1202SC23K2500 awarded to PERIMETER SOLUTIONS LP for the amount of $5,000,000"
# Переменная: title
# Описание: Краткое текстовое описание контракта.
# Формат: Строка (String).
# Важность для анализа: Низкая – содержит дублирующуюся информацию, которая уже представлена в других полях.

"contract_type": "AWARD"
# Переменная: `contract_type`
# Описание: Тип контракта (например, AWARD, IDV, OTHERTRANSACTIONAWARD, OTHERTRANSACTIONIDV).
# Формат: Строка (String).
# Важность для анализа: `Высокая` – помогает классифицировать контракт по типу.

"link__rel": "alternate"
# Переменная: link__rel
# Описание: Определяет тип ссылки, указывая, что это альтернативный источник информации о контракте.
# Формат: Строка (String).
# Важность для анализа: Низкая – в большинстве случаев не влияет на анализ контракта.

"link__type": "text/html"
# Переменная: link__type
# Описание: Указывает формат содержимого ссылки (в данном случае HTML-страница).
# Формат: Строка (String).
# Важность для анализа: Низкая – не влияет на анализ контракта, но полезна для работы с веб-ссылками.

"link__href": "https://www.fpds.gov/ezsearch/search.do?s=FPDS&indexName=awardfull&templateName=1.5.3&q=1202SC23K2500+12C2+"
# Переменная: link__href
# Описание: URL-адрес, ведущий на страницу с детальной информацией о контракте в FPDS.
# Формат: Строка (URL).
# Важность для анализа: Средняя – полезна для получения дополнительной информации о контракте, но не критична для структурированного анализа.

"modified": "2023-02-07 15:12:28"
# Переменная: `modified`
# Описание: Дата и время последнего изменения данных о контракте.
# Формат: TIMESTAMP (YYYY-MM-DD HH:MM:SS).
# Важность для анализа: `Высокая` – позволяет отслеживать актуальность данных и изменения в контракте.

"content": "\n      "

"content__type": "application/xml"
# Переменная: content__type
# Описание: Указывает формат данных внутри 'content', в данном случае XML.
# Формат: Строка (String).
# Важность для анализа: Низкая – полезно только для определения формата данных, не несёт важной аналитической информации.

"content__award": "\n        "
"content__award__version": "1.5"
# Переменная: content__award__version
# Описание: Версия схемы данных контракта в FPDS.
# Формат: Строка (String).
# Важность для анализа: Низкая – важно только при анализе изменений структуры данных FPDS.

"content__award__awardID": "\n"
"content__award__awardID__awardContractID": "\n            "

"content__award__awardID__awardContractID__agencyID": "12C2"
# Переменная: `agency_id`
# Описание: Код агентства, заключившего контракт.
# Формат: Строка (String).
# Важность для анализа: `Высокая` – позволяет определить, какое агентство отвечает за контракт.

"content__award__awardID__awardContractID__agencyID__name": "FOREST SERVICE"
# Переменная: content__award__awardID__awardContractID__agencyID__name
# Описание: Название агентства, заключившего контракт.
# Формат: Строка (String).
# Важность для анализа: Средняя – дублирует 'agencyID', но полезна для удобочитаемости.

"content__award__awardID__awardContractID__PIID": "1202SC23K2500"
# Переменная: `piid`
# Описание: Уникальный идентификатор контракта (Procurement Instrument Identifier, PIID).
# Формат: Строка (String).
# Важность для анализа: `Высокая` – основной идентификатор контракта, необходимый для поиска и анализа.

"content__award__awardID__awardContractID__modNumber": "0"
# Переменная: `mod_number`
# Описание: Номер модификации контракта.
# Формат: Строка (String).
# Важность для анализа: `Высокая` – если модификация ≠ 0, важно для отслеживания изменений в контракте.

"content__award__awardID__awardContractID__transactionNumber": "0"
# Переменная: content__award__awardID__awardContractID__transactionNumber
# Описание: Номер транзакции в рамках контракта (может указывать на уникальные события, связанные с контрактом).
# Формат: Строка (String), обычно числовое значение.
# Важность для анализа: Низкая – редко используется отдельно, но может быть полезна в сложных анализах.

"content__award__awardID__referencedIDVID": "\n            "

"content__award__awardID__referencedIDVID__agencyID": "12C2"
# Переменная: content__award__awardID__referencedIDVID__agencyID
# Описание: Код агентства, выдавшего связанный IDV-контракт.
# Формат: Строка (String).
# Важность для анализа: Средняя – если контракт связан с IDV, полезно для понимания структуры контрактов.

"content__award__awardID__referencedIDVID__agencyID__name": "FOREST SERVICE"
# Переменная: content__award__awardID__referencedIDVID__agencyID__name
# Описание: Название агентства, выдавшего связанный IDV-контракт.
# Формат: Строка (String).
# Важность для анализа: Средняя – удобно для читаемости, но дублирует 'referencedIDVID__agencyID'.

"content__award__awardID__referencedIDVID__PIID": "12024B18D9025"
# Переменная: `referenced_piid`
# Описание: PIID для родительского контракта
# Формат: Строка (String).
# Важность для анализа: `Высокая` – важен для отслеживания структуры контрактов и их связей.

"content__award__awardID__referencedIDVID__modNumber": "0"
# Переменная: content__award__awardID__referencedIDVID__modNumber
# Описание: Номер модификации связанного IDV-контракта.
# Формат: Строка (String), обычно числовое значение.
# Важность для анализа: Средняя – если не "0", означает, что IDV-контракт был модифицирован.

"content__award__relevantContractDates": "\n          "

"content__award__relevantContractDates__signedDate": "2023-01-01 00:00:00"
# Переменная: `signed_date`
# Описание: Дата подписания контракта.
# Формат: Дата и время (YYYY-MM-DD).
# Важность для анализа: `Высокая` – фиксирует момент заключения контракта.

"content__award__relevantContractDates__effectiveDate": "2023-01-01 00:00:00"
# Переменная: `effective_date`
# Описание: Дата вступления контракта в силу.
# Формат: Дата и время (YYYY-MM-DD).
# Важность для анализа: `Высокая` – важно для расчёта сроков действия контракта.

"content__award__relevantContractDates__currentCompletionDate": "2023-12-31 00:00:00"
# Переменная: content__award__relevantContractDates__currentCompletionDate
# Описание: Текущая дата завершения контракта (может изменяться в ходе выполнения).
# Формат: Дата и время (YYYY-MM-DD).
# Важность для анализа: Средняя – показывает ожидаемую дату окончания контракта.

"content__award__relevantContractDates__ultimateCompletionDate": "2023-12-31 00:00:00"
# Переменная: `ultimate_completion_date`
# Описание: Окончательная дата завершения контракта, учитывая все возможные продления.
# Формат: Дата и время (YYYY-MM-DD).
# Важность для анализа: `Высокая` – определяет максимальный срок действия контракта.

"content__award__dollarValues": "\n          "

"content__award__dollarValues__obligatedAmount": "5000000.00"
# Переменная: `obligated_amount`
# Описание: Сумма, фактически выделенная по контракту (обязательства по оплате).
# Формат: Число с двумя знаками после запятой (Decimal).
# Важность для анализа: `Высокая` – определяет реальную сумму финансирования.

"content__award__dollarValues__baseAndExercisedOptionsValue": "5000000.00"
# Переменная: content__award__dollarValues__baseAndExercisedOptionsValue
# Описание: Сумма базового контракта плюс все активированные (использованные) опции.
# Формат: Число с двумя знаками после запятой (Decimal).
# Важность для анализа: Средняя – полезно для понимания общей стоимости контракта с учётом использованных опций.

"content__award__dollarValues__baseAndAllOptionsValue": "5000000.00"
# Переменная: `base_and_all_options_value`
# Описание: Полная стоимость контракта, включая все возможные опции (даже если они ещё не активированы).
# Формат: Число с двумя знаками после запятой (Decimal).
# Важность для анализа: `Высокая` – помогает понять максимальный бюджет контракта.

"content__award__totalDollarValues": "\n          "

"content__award__totalDollarValues__totalObligatedAmount": "5000000.00"
# Переменная: `total_obligated_amount`
# Описание: Общая сумма, выделенная по контракту (включает все модификации и изменения).
# Формат: Число с двумя знаками после запятой (Decimal).
# Важность для анализа: `Высокая` – ключевой показатель фактического финансирования контракта.

"content__award__totalDollarValues__totalBaseAndExercisedOptionsValue": "5000000.00"
# Переменная: content__award__totalDollarValues__totalBaseAndExercisedOptionsValue
# Описание: Общая стоимость базового контракта и всех использованных (активированных) опций.
# Формат: Число с двумя знаками после запятой (Decimal).
# Важность для анализа: Средняя – помогает оценить, насколько контракт использует доступные опции.

"content__award__totalDollarValues__totalBaseAndAllOptionsValue": "5000000.00"
# Переменная: `total_base_and_all_options_value`
# Описание: Полная стоимость контракта, включая базовую сумму и все возможные опции (даже если они не активированы).
# Формат: Число с двумя знаками после запятой (Decimal).
# Важность для анализа: `Высокая` – позволяет понять максимально возможные затраты по контракту.

"content__award__purchaserInformation": "\n          "

"content__award__purchaserInformation__contractingOfficeAgencyID": "12C2"
# Переменная: `contracting_office_agency_id`
# Описание: Код агентства, заключившего контракт.
# Формат: Строка (String).
# Важность для анализа: `Высокая` – позволяет идентифицировать организацию-заказчика.

"content__award__purchaserInformation__contractingOfficeAgencyID__name": "FOREST SERVICE"
# Переменная: content__award__purchaserInformation__contractingOfficeAgencyID__name
# Описание: Название агентства, заключившего контракт.
# Формат: Строка (String).
# Важность для анализа: Средняя – дублирует 'contractingOfficeAgencyID', но удобна для читаемости.

"content__award__purchaserInformation__contractingOfficeAgencyID__departmentID": "1200"
# Переменная: content__award__purchaserInformation__contractingOfficeAgencyID__departmentID
# Описание: Код департамента, к которому относится агентство-заказчик.
# Формат: Строка (String).
# Важность для анализа: Средняя – полезно для анализа по департаментам, но не всегда критично.

"content__award__purchaserInformation__contractingOfficeAgencyID__departmentName": "AGRICULTURE, DEPARTMENT OF"
# Переменная: content__award__purchaserInformation__contractingOfficeAgencyID__departmentName
# Описание: Название департамента, к которому относится агентство-заказчик.
# Формат: Строка (String).
# Важность для анализа: Средняя – полезно для группировки контрактов по департаментам, но может дублировать другие поля.

"content__award__purchaserInformation__contractingOfficeID": "1202SC"
# Переменная: `contracting_office_id`
# Описание: Код контрактного офиса, который оформил контракт.
# Формат: Строка (String).
# Важность для анализа: `Высокая` – позволяет идентифицировать конкретный офис, занимающийся закупками.

"content__award__purchaserInformation__contractingOfficeID__name": "USDA-FS, INCIDENT PROCUREMENT LOGISTICS"
# Переменная: content__award__purchaserInformation__contractingOfficeID__name
# Описание: Название контрактного офиса, заключившего контракт.
# Формат: Строка (String).
# Важность для анализа: Средняя – удобно для читаемости, но может дублировать 'contractingOfficeID'.

"content__award__purchaserInformation__contractingOfficeID__regionCode": "25"
# Переменная: content__award__purchaserInformation__contractingOfficeID__regionCode
# Описание: Код региона контрактного офиса.
# Формат: Строка (String), обычно числовое значение.
# Важность для анализа: Средняя – может быть полезно для географического анализа распределения контрактов.

"content__award__purchaserInformation__contractingOfficeID__country": "USA"
# Переменная: content__award__purchaserInformation__contractingOfficeID__country
# Описание: Страна, в которой расположен контрактный офис.
# Формат: Строка (String).
# Важность для анализа: Низкая – почти всегда будет "USA", если контракт заключён в США.

"content__award__purchaserInformation__fundingRequestingAgencyID": "12C2"
# Переменная: `funding_requesting_agency_id`
# Описание: Код агентства, запрашивающего финансирование для контракта.
# Формат: Строка (String).
# Важность для анализа: `Высокая` – позволяет определить организацию, финансирующую контракт.

"content__award__purchaserInformation__fundingRequestingAgencyID__name": "FOREST SERVICE"
# Переменная: content__award__purchaserInformation__fundingRequestingAgencyID__name
# Описание: Название агентства, запрашивающего финансирование.
# Формат: Строка (String).
# Важность для анализа: Средняя – дублирует 'fundingRequestingAgencyID', но улучшает читаемость.

"content__award__purchaserInformation__fundingRequestingAgencyID__departmentID": "1200"
# Переменная: content__award__purchaserInformation__fundingRequestingAgencyID__departmentID
# Описание: Код департамента, к которому относится финансирующее агентство.
# Формат: Строка (String).
# Важность для анализа: Средняя – полезно для классификации контрактов по департаментам.

"content__award__purchaserInformation__fundingRequestingAgencyID__departmentName": "AGRICULTURE, DEPARTMENT OF"
# Переменная: content__award__purchaserInformation__fundingRequestingAgencyID__departmentName
# Описание: Название департамента, к которому относится финансирующее агентство.
# Формат: Строка (String).
# Важность для анализа: Средняя – помогает группировать контракты по департаментам.

"content__award__purchaserInformation__fundingRequestingOfficeID": "12024B"
# Переменная: `funding_requesting_office_id`
# Описание: Код офиса, запрашивающего финансирование для контракта.
# Формат: Строка (String).
# Важность для анализа: `Высокая` – позволяет определить конкретный офис, ответственный за финансирование.

"content__award__purchaserInformation__fundingRequestingOfficeID__name": "USDA FOREST SERVICE"
# Переменная: content__award__purchaserInformation__fundingRequestingOfficeID__name
# Описание: Название офиса, запрашивающего финансирование.
# Формат: Строка (String).
# Важность для анализа: Средняя – дублирует 'fundingRequestingOfficeID', но улучшает читаемость.

"content__award__purchaserInformation__foreignFunding": "X"
# Переменная: content__award__purchaserInformation__foreignFunding
# Описание: Указывает, используется ли иностранное финансирование.
# Формат: Строка (String), обычно "X" означает "NOT APPLICABLE".
# Важность для анализа: Средняя – может быть важна при анализе международного финансирования.

"content__award__purchaserInformation__foreignFunding__description": "NOT APPLICABLE"
# Переменная: content__award__purchaserInformation__foreignFunding__description
# Описание: Описание статуса иностранного финансирования (в данном случае отсутствует).
# Формат: Строка (String).
# Важность для анализа: Низкая – уточняет значение 'foreignFunding', если оно всегда "NOT APPLICABLE", поле можно игнорировать.

"content__award__contractMarketingData": "\n          "

"content__award__contractMarketingData__feePaidForUseOfService": "0.00"
# Переменная: content__award__contractMarketingData__feePaidForUseOfService
# Описание: Размер комиссии, уплаченной за использование сервиса (если применимо).
# Формат: Число с двумя знаками после запятой (Decimal).
# Важность для анализа: Низкая – если всегда "0.00", не представляет аналитической ценности.

"content__award__contractData": "\n          "

"content__award__contractData__contractActionType": "C"
# Переменная: content__award__contractData__contractActionType
# Описание: Код типа действия по контракту.
# Формат: Строка (String).
# Важность для анализа: Средняя – полезно для классификации контрактов, но более важен 'contractActionType__description'.

"content__award__contractData__contractActionType__description": "DELIVERY ORDER"
# Переменная: `contract_action_type_description`
# Описание: Описание типа действия по контракту.
# Формат: Строка (String).
# Важность для анализа: `Высокая` – ключевая информация о том, каким образом оформлен контракт.

"content__award__contractData__typeOfContractPricing": "J"
# Переменная: content__award__contractData__typeOfContractPricing
# Описание: Код типа ценообразования по контракту.
# Формат: Строка (String).
# Важность для анализа: Средняя – полезно при обработке данных, но более важно описание.

"content__award__contractData__typeOfContractPricing__description": "FIRM FIXED PRICE"
# Переменная: `type_of_contract_pricing_description`
# Описание: Тип ценообразования.
# Формат: Строка (String).
# Важность для анализа: `Высокая` – определяет, как формируется стоимость контракта.
Примеры значений:
- “FIRM FIXED PRICE”: фиксированная цена
- “COST REIMBURSEMENT”: возмещение затрат
- “TIME AND MATERIALS”: время и материалы
- “FIXED PRICE WITH ECONOMIC PRICE ADJUSTMENT”: фиксированная цена с экономической корректировкой
- “INCENTIVE CONTRACT”: контракт с элементами стимулирования
- “AWARD FEE CONTRACT”: контракт с наградной платой

"content__award__contractData__majorProgramCode": "NATIONAL RETARDANT - BULK"
# Переменная: content__award__contractData__majorProgramCode
# Описание: Основной код программы, к которой относится контракт (в данном случае – массовые закупки огнегасящего вещества).
# Формат: Строка (String).
# Важность для анализа: Средняя – полезно для классификации контрактов, но не всегда критично.

"content__award__contractData__nationalInterestActionCode": "NONE"
# Переменная: content__award__contractData__nationalInterestActionCode
# Описание: Код, указывающий, связан ли контракт с национальными интересами, такими как чрезвычайные ситуации, военные операции или экономические стимулы.
# Формат: Строка (String).
# Важность для анализа: Средняя – если значение **не "NONE"**, может указывать на важные государственные приоритеты.

"content__award__contractData__nationalInterestActionCode__description": "NONE"
# Переменная: content__award__contractData__nationalInterestActionCode__description
# Описание: Описание кода национального интереса (в данном случае – нет связи с национальными интересами).
# Формат: Строка (String).
# Важность для анализа: Низкая – только подтверждает, что контракт не связан с приоритетными национальными программами.

"content__award__contractData__costOrPricingData": "N"
# Переменная: content__award__contractData__costOrPricingData
# Описание: Указывает, предоставлялись ли данные о стоимости и ценообразовании при заключении контракта.
# Формат: Строка (String), обычно "Y" (Yes) или "N" (No).
# Важность для анализа: Средняя – помогает определить, требовались ли расчёты стоимости перед заключением контракта.

"content__award__contractData__costOrPricingData__description": "No"
# Переменная: content__award__contractData__costOrPricingData__description
# Описание: Текстовое описание значения 'costOrPricingData'.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует 'costOrPricingData', полезно только для удобства чтения.

"content__award__contractData__costAccountingStandardsClause": "X"
# Переменная: content__award__contractData__costAccountingStandardsClause
# Описание: Указывает, применяется ли к контракту стандарт учёта затрат (Cost Accounting Standards - CAS).
# Формат: Строка (String).
# Важность для анализа: Средняя – важно для определения правил учёта затрат по контракту.

"content__award__contractData__costAccountingStandardsClause__description": "NOT APPLICABLE EXEMPT FROM CAS"
# Переменная: content__award__contractData__costAccountingStandardsClause__description
# Описание: Описание того, применяется ли CAS к контракту (в данном случае контракт освобождён от CAS).
# Формат: Строка (String).
# Важность для анализа: Средняя – уточняет, подпадает ли контракт под регулирование учёта затрат.

"content__award__contractData__descriptionOfContractRequirement": "NATIONAL RETARDANT - BULK 2023 INITIAL OBLIGATION"
# Переменная: `description_of_contract_requirement`
# Описание: Описание требований к контракту – цель и предмет закупки.
# Формат: Строка (String).
# Важность для анализа: `Высокая` – ключевое поле, объясняющее суть контракта.

"content__award__contractData__inherentlyGovernmentalFunction": "OT        "
# Переменная: content__award__contractData__inherentlyGovernmentalFunction
# Описание: Код, указывающий, выполняет ли контракт функции, которые должны оставаться в руках правительства.
# Формат: Строка (String), возможные значения:
# Важность для анализа: Средняя – если значение "IG", контракт может требовать повышенного контроля.

"content__award__contractData__inherentlyGovernmentalFunction__description": "OTHER FUNCTIONS"
# Переменная: content__award__contractData__inherentlyGovernmentalFunction__description
# Описание: Описание того, относятся ли функции контракта к исключительно государственным.
# Формат: Строка (String).
# Важность для анализа: Средняя – если указано "INHERENTLY GOVERNMENTAL", контракт должен выполняться только госслужащими.

"content__award__contractData__GFE-GFP": "N"
# Переменная: content__award__contractData__GFE-GFP
# Описание: Указывает, используется ли в контракте государственное оборудование или имущество (Government-Furnished Equipment/Government-Furnished Property).
# Формат: Строка (String), обычно "Y" (Yes) или "N" (No).
# Важность для анализа: Средняя – если "Y", контракт включает использование государственного имущества.

"content__award__contractData__GFE-GFP__description": "Transaction does not use GFE/GFP"
# Переменная: content__award__contractData__GFE-GFP__description
# Описание: Текстовое описание значения 'GFE-GFP', указывающее, используется ли государственное имущество.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует 'GFE-GFP', полезно для удобства чтения.

"content__award__contractData__undefinitizedAction": "X"
# Переменная: content__award__contractData__undefinitizedAction
# Описание: Указывает, является ли действие по контракту "неопределённым" (Undefinitized Contract Action, UCA) – когда работа начинается до окончательного соглашения о стоимости.
# Формат: Строка (String), обычно "Y" (Yes) или "X" (No).
# Важность для анализа: Средняя – если "Y", означает, что контракт может содержать неопределённые условия.

"content__award__contractData__undefinitizedAction__description": "NO"
# Переменная: content__award__contractData__undefinitizedAction__description
# Описание: Описание, содержит ли контракт неопределённые условия.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует 'undefinitizedAction', полезно для удобочитаемости.

"content__award__contractData__consolidatedContract": "D"
# Переменная: content__award__contractData__consolidatedContract
# Описание: Указывает, является ли контракт консолидированным (объединяет несколько контрактов или требований в один).
# Формат: Строка (String), возможные значения:
# Важность для анализа: Средняя – важно при анализе крупных контрактов, объединяющих несколько потребностей.

"content__award__contractData__consolidatedContract__description": "NOT CONSOLIDATED"
# Переменная: content__award__contractData__consolidatedContract__description
# Описание: Указывает, является ли контракт консолидированным (объединяющим несколько контрактов в один).
# Формат: Строка (String).
# Важность для анализа: Средняя – влияет на анализ закупок, особенно крупных контрактов.

"content__award__contractData__performanceBasedServiceContract": "N"
# Переменная: content__award__contractData__performanceBasedServiceContract
# Описание: Указывает, является ли контракт сервисным контрактом, основанным на показателях эффективности (Performance-Based Acquisition, PBA).
# Формат: Строка (String).
# Важность для анализа: Средняя – важно для анализа качества услуг, поставляемых по контракту.

"content__award__contractData__performanceBasedServiceContract__description": "NO - SERVICE WHERE PBA IS NOT USED."
# Переменная: content__award__contractData__performanceBasedServiceContract__description
# Описание: Текстовое описание значения 'performanceBasedServiceContract', уточняющее, применяется ли Performance-Based Acquisition.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует 'performanceBasedServiceContract', полезно для удобочитаемости.

"content__award__contractData__multiYearContract": "N"
# Переменная: `multi_year_contract`
# Описание: Указывает, является ли контракт многолетним.
# Формат: Строка (String).
# Важность для анализа: `Высокая` – многолетние контракты важны для долгосрочного бюджетного планирования.

"content__award__contractData__multiYearContract__description": "NO"
# Переменная: content__award__contractData__multiYearContract__description
# Описание: Текстовое описание значения 'multiYearContract', уточняющее, является ли контракт многолетним.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует 'multiYearContract', полезно для удобочитаемости.

"content__award__contractData__contingencyHumanitarianPeacekeepingOperation": "X"
# Переменная: content__award__contractData__contingencyHumanitarianPeacekeepingOperation
# Описание: Указывает, связан ли контракт с операциями по чрезвычайным ситуациям, гуманитарной помощи или миротворчеству.
# Формат: Строка (String).
# Важность для анализа: Средняя – может быть важно при анализе контрактов в рамках государственных и военных программ.

"content__award__contractData__contingencyHumanitarianPeacekeepingOperation__description": "NOT APPLICABLE"
# Переменная: content__award__contractData__contingencyHumanitarianPeacekeepingOperation__description
# Описание: Описание значения 'contingencyHumanitarianPeacekeepingOperation', указывающее, связан ли контракт с гуманитарными операциями.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__contractData__referencedIDVMultipleOrSingle": "S"
# Переменная: `referenced_idv_multiple_or_single`
# Описание: Указывает, является ли связанный IDV (Indefinite Delivery Vehicle) контрактом с одним или несколькими поставщиками.
# Формат: Строка (String).
# Важность для анализа: `Высокая` – важно для понимания структуры контрактов и конкуренции.

"content__award__contractData__referencedIDVMultipleOrSingle__description": "SINGLE AWARD"
# Переменная: content__award__contractData__referencedIDVMultipleOrSingle__description
# Описание: Описание значения 'referencedIDVMultipleOrSingle', уточняющее тип присуждения контракта.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__contractData__referencedIDVType": "B"
# Переменная: `referenced_idv_type`
# Описание: Указывает тип IDV-контракта (Indefinite Delivery Vehicle).
# Формат: Строка (String).
# Важность для анализа: `Высокая` – важно при анализе типов контрактов и их условий.
Примеры значений:
- B – Basic Ordering Agreement (BOA)
- D – Definite Quantity Contract (DQC)
- F – Indefinite Quantity Contract (IQC)
- G – Indefinite Delivery/Indefinite Quantity (IDIQ)
- J – Basic Agreement
- M – Multi-Year Contract
- P – Requirements Contract

"content__award__contractData__referencedIDVType__description": "IDC"
# Переменная: content__award__contractData__referencedIDVType__description
# Описание: Описание значения 'referencedIDVType', уточняющее тип IDV-контракта.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__contractData__contractFinancing": "Z"
# Переменная: content__award__contractData__contractFinancing
# Описание: Указывает, используется ли в контракте механизм финансирования.
# Формат: Строка (String).
# Важность для анализа: Средняя – важно, если контракт связан с предоплатой или частным финансированием.

"content__award__contractData__contractFinancing__description": "NOT APPLICABLE"
# Переменная: content__award__contractData__contractFinancing__description
# Описание: Описание значения 'contractFinancing', указывающее, используется ли механизм финансирования в контракте.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле 'contractFinancing', полезно для удобочитаемости.

"content__award__contractData__purchaseCardAsPaymentMethod": "N"
# Переменная: content__award__contractData__purchaseCardAsPaymentMethod
# Описание: Указывает, используется ли в качестве метода оплаты правительственная покупательная карта (Government Purchase Card).
# Формат: Строка (String).
# Важность для анализа: Средняя – важно для определения механизмов расчёта по контракту.

"content__award__contractData__purchaseCardAsPaymentMethod__description": "NO"
# Переменная: content__award__contractData__purchaseCardAsPaymentMethod__description
# Описание: Описание значения 'purchaseCardAsPaymentMethod', уточняющее, используется ли покупательная карта.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__contractData__numberOfActions": "1"
# Переменная: content__award__contractData__numberOfActions
# Описание: Количество действий (транзакций) по данному контракту.
# Формат: Целое число (Integer).
# Важность для анализа: Средняя – полезно для отслеживания количества операций по контракту.

"content__award__legislativeMandates": "\n          "

"content__award__legislativeMandates__ClingerCohenAct": "N"
# Переменная: content__award__legislativeMandates__ClingerCohenAct
# Описание: Указывает, применяется ли к контракту Закон Клинжера-Коэна (Clinger-Cohen Act), регулирующий IT-закупки в федеральных агентствах.
# Формат: Строка (String).
# Важность для анализа: Средняя – важно, если контракт связан с IT-закупками.

"content__award__legislativeMandates__ClingerCohenAct__description": "NO"
# Переменная: content__award__legislativeMandates__ClingerCohenAct__description
# Описание: Описание значения 'ClingerCohenAct', уточняющее, применяется ли это законодательство.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__legislativeMandates__materialsSuppliesArticlesEquipment": "N"
# Переменная: content__award__legislativeMandates__materialsSuppliesArticlesEquipment
# Описание: Указывает, регулируется ли контракт законодательством, касающимся поставки материалов, оборудования и товаров.
# Формат: Строка (String).
# Важность для анализа: Средняя – важно при анализе контрактов, связанных с поставками оборудования.

"content__award__legislativeMandates__materialsSuppliesArticlesEquipment__description": "NO"
# Переменная: content__award__legislativeMandates__materialsSuppliesArticlesEquipment__description
# Описание: Описание значения 'materialsSuppliesArticlesEquipment', указывающее, регулируется ли контракт поставками материалов и оборудования.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__legislativeMandates__laborStandards": "Y"
# Переменная: `labor_standards`
# Описание: Указывает, применяются ли к контракту требования по стандартам труда.
# Формат: Строка (String).
# Важность для анализа: `Высокая` – важно при анализе контрактов, связанных с наёмным трудом и минимальными стандартами оплаты.

"content__award__legislativeMandates__laborStandards__description": "YES"
# Переменная: content__award__legislativeMandates__laborStandards__description
# Описание: Описание значения 'laborStandards', уточняющее, применяются ли стандарты труда.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__legislativeMandates__constructionWageRateRequirements": "N"
# Переменная: content__award__legislativeMandates__constructionWageRateRequirements
# Описание: Указывает, регулируется ли контракт требованиями к оплате труда в строительной отрасли (Davis-Bacon Act).
# Формат: Строка (String).
# Важность для анализа: Средняя – важно для строительных контрактов и оценки условий оплаты труда.

"content__award__legislativeMandates__constructionWageRateRequirements__description": "NO"
# Переменная: content__award__legislativeMandates__constructionWageRateRequirements__description
# Описание: Описание значения 'constructionWageRateRequirements', уточняющее, регулируется ли контракт требованиями по ставкам оплаты в строительстве.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__legislativeMandates__listOfAdditionalReportingValues": "\n            "
# Переменная: content__award__legislativeMandates__listOfAdditionalReportingValues
# Описание: Контейнер для списка дополнительных отчетных требований, применимых к контракту.
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – само поле не содержит информации, но вложенные элементы могут быть полезны.

"content__award__legislativeMandates__listOfAdditionalReportingValues__additionalReportingValue": "S"
# Переменная: content__award__legislativeMandates__listOfAdditionalReportingValues__additionalReportingValue
# Описание: Код, указывающий дополнительные требования к отчетности по контракту.
# Формат: Строка (String).
# Важность для анализа: Средняя – важно для определения дополнительных обязательств подрядчика.

"content__award__legislativeMandates__listOfAdditionalReportingValues__additionalReportingValue__description": "SERVICE CONTRACT INVENTORY (FAR 4.17)"
# Переменная: content__award__legislativeMandates__listOfAdditionalReportingValues__additionalReportingValue__description
# Описание: Описание кода 'additionalReportingValue', уточняющее, какое требование по отчетности применяется.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__legislativeMandates__interagencyContractingAuthority": "X"
# Переменная: content__award__legislativeMandates__interagencyContractingAuthority
# Описание: Указывает, регулируется ли контракт межведомственным соглашением (Interagency Contracting Authority).
# Формат: Строка (String).
# Важность для анализа: Средняя – важно, если контракт заключён в рамках совместных закупок между агентствами.

"content__award__legislativeMandates__interagencyContractingAuthority__description": "NOT APPLICABLE"
# Переменная: content__award__legislativeMandates__interagencyContractingAuthority__description
# Описание: Описание значения 'interagencyContractingAuthority', уточняющее, подпадает ли контракт под межведомственное соглашение.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__productOrServiceInformation": "\n          "

"content__award__productOrServiceInformation__productOrServiceCode": "F003"
# Переменная: `psc_code`
# Описание: Код, обозначающий тип продукции или услуги, предоставляемой по контракту.
# Формат: Строка (String).
# Важность для анализа: `Высокая` – важно для классификации контрактов.

"content__award__productOrServiceInformation__productOrServiceCode__description": "NATURAL RESOURCES/CONSERVATION- FOREST-RANGE FIRE SUPPRESSION/PRESUPPRESSION"
# Переменная: content__award__productOrServiceInformation__productOrServiceCode__description
# Описание: Описание кода 'productOrServiceCode', уточняющее, какие услуги или товары включает контракт.
# Формат: Строка (String).
# Важность для анализа: Средняя – полезно для интерпретации 'productOrServiceCode', но можно заменить справочником кодов.

"content__award__productOrServiceInformation__productOrServiceCode__productOrServiceType": "SERVICE"
# Переменная: `psc_type`
# Описание: Определяет, относится ли контракт к категории "товары" (Product) или "услуги" (Service).
# Формат: Строка (String).
# Важность для анализа: `Высокая` – помогает классифицировать контракты по типу.

"content__award__productOrServiceInformation__contractBundling": "H"
# Переменная: content__award__productOrServiceInformation__contractBundling
# Описание: Указывает, является ли контракт "bundled" (объединённым из нескольких меньших контрактов).
# Формат: Строка (String).
# Важность для анализа: Средняя – важно при анализе влияния на малый бизнес и конкуренцию.

"content__award__productOrServiceInformation__contractBundling__description": "NOT BUNDLED"
# Переменная: content__award__productOrServiceInformation__contractBundling__description
# Описание: Описание значения 'contractBundling', указывающее, является ли контракт объединённым.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__productOrServiceInformation__principalNAICSCode": "115310"
# Переменная: `naics_code`
# Описание: Основной код отрасли по системе NAICS (North American Industry Classification System).
# Формат: Строка (String).
# Важность для анализа: `Высокая` – позволяет анализировать контракты по отраслям.

"content__award__productOrServiceInformation__principalNAICSCode__description": "SUPPORT ACTIVITIES FOR FORESTRY"
# Переменная: content__award__productOrServiceInformation__principalNAICSCode__description
# Описание: Описание кода NAICS, указывающее, к какой отрасли относится контракт.
# Формат: Строка (String).
# Важность для анализа: Средняя – дублирует код NAICS, но делает его понятнее.

"content__award__productOrServiceInformation__recoveredMaterialClauses": "E"
# Переменная: content__award__productOrServiceInformation__recoveredMaterialClauses
# Описание: Указывает, есть ли требования по использованию переработанных материалов.
# Формат: Строка (String).
# Важность для анализа: Средняя – важно при анализе экологических контрактов.

"content__award__productOrServiceInformation__recoveredMaterialClauses__description": "BIO-BASED"
# Переменная: content__award__productOrServiceInformation__recoveredMaterialClauses__description
# Описание: Описание требований по использованию переработанных или био-материалов.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__productOrServiceInformation__manufacturingOrganizationType": "C"
# Переменная: content__award__productOrServiceInformation__manufacturingOrganizationType
# Описание: Указывает тип организации-производителя, если применимо.
# Формат: Строка (String).
# Важность для анализа: Средняя – важно при анализе контрактов с иностранными поставщиками.

"content__award__productOrServiceInformation__manufacturingOrganizationType__description": "FOREIGN-OWNED BUSINESS INCORPORATED IN THE U.S."
# Переменная: content__award__productOrServiceInformation__manufacturingOrganizationType__description
# Описание: Описание типа организации-производителя, уточняющее, является ли компания иностранной или национальной.
# Формат: Строка (String).
# Важность для анализа: Средняя – полезно при анализе участия иностранных компаний в госзакупках.

"content__award__productOrServiceInformation__useOfEPADesignatedProducts": "E"
# Переменная: content__award__productOrServiceInformation__useOfEPADesignatedProducts
# Описание: Указывает, требует ли контракт использование продуктов, сертифицированных Агентством по охране окружающей среды (EPA).
# Формат: Строка (String).
# Важность для анализа: Средняя – важно при анализе контрактов, связанных с экологическими стандартами.

"content__award__productOrServiceInformation__useOfEPADesignatedProducts__description": "NOT REQUIRED"
# Переменная: content__award__productOrServiceInformation__useOfEPADesignatedProducts__description
# Описание: Описание значения 'useOfEPADesignatedProducts', уточняющее, требуется ли использование утверждённых EPA продуктов.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__productOrServiceInformation__countryOfOrigin": "USA"
# Переменная: `country_of_origin`
# Описание: Код страны происхождения товара или услуги.
# Формат: Строка (String).
# Важность для анализа: `Высокая` – важно при анализе импорта и национального производства.

"content__award__productOrServiceInformation__countryOfOrigin__name": "UNITED STATES"
# Переменная: content__award__productOrServiceInformation__countryOfOrigin__name
# Описание: Название страны происхождения товара или услуги.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует код страны, полезно для удобочитаемости.

"content__award__productOrServiceInformation__placeOfManufacture": "C"
# Переменная: content__award__productOrServiceInformation__placeOfManufacture
# Описание: Указывает, является ли контрактным предметом готовый производственный продукт.
# Формат: Строка (String).
# Важность для анализа: Средняя – полезно при анализе контрактов на производство.

"content__award__productOrServiceInformation__placeOfManufacture__description": "NOT A MANUFACTURED END PRODUCT"
# Переменная: content__award__productOrServiceInformation__placeOfManufacture__description
# Описание: Описание значения 'placeOfManufacture', уточняющее, является ли товар конечным продуктом производства.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__vendor": "\n          "
"content__award__vendor__vendorHeader": "\n            "

"content__award__vendor__vendorHeader__vendorName": "PERIMETER SOLUTIONS LP"
# Переменная: `vendor_name`
# Описание: Официальное название поставщика, заключившего контракт.
# Формат: Строка (String).
# Важность для анализа: `Высокая` – ключевая информация о подрядчике.

"content__award__vendor__vendorSiteDetails": "\n            "
"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators": "\n              "

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isAlaskanNativeOwnedCorporationOrFirm": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isAlaskanNativeOwnedCorporationOrFirm
# Описание: Указывает, является ли компания корпорацией или фирмой, принадлежащей коренным жителям Аляски.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для контрактов, выделяемых для поддержки коренных народов.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isAmericanIndianOwned": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isAmericanIndianOwned
# Описание: Указывает, принадлежит ли компания представителю коренного населения Америки.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для контрактов, выделяемых для поддержки коренных американцев.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isIndianTribe": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isIndianTribe
# Описание: Указывает, является ли компания предприятием, принадлежащим индейскому племени.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – может быть важным для контрактов, предоставляемых племенным организациям.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isNativeHawaiianOwnedOrganizationOrFirm": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isNativeHawaiianOwnedOrganizationOrFirm
# Описание: Указывает, принадлежит ли компания представителям коренного населения Гавайев.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно при анализе контрактов, поддерживающих бизнес коренных гавайцев.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isTriballyOwnedFirm": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isTriballyOwnedFirm
# Описание: Указывает, принадлежит ли компания племенной организации.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – используется при выделении контрактов для племенных организаций.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isSmallBusiness": "false"
# Переменная: `is_small_business`
# Описание: Указывает, относится ли компания к категории малого бизнеса.
# Формат: Булево (Boolean).
# Важность для анализа: `Высокая` – важно для контрактов, выделяемых в рамках программ поддержки малого бизнеса.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isVeteranOwned": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isVeteranOwned
# Описание: Указывает, принадлежит ли компания ветерану вооружённых сил США.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно при анализе контрактов, выделяемых для ветеранов.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isServiceRelatedDisabledVeteranOwnedBusiness": "false"
# Переменная: `is_service_related_disabled_veteran_owned_business`
# Описание: Указывает, принадлежит ли компания ветерану с ограниченными возможностями, связанными со службой.
# Формат: Булево (Boolean).
# Важность для анализа: `Высокая` – имеет значение для контрактов, выделяемых в поддержку ветеранов-инвалидов.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isWomenOwned": "false"
# Переменная: `is_women_owned`
# Описание: Указывает, принадлежит ли компания женщине.
# Формат: Булево (Boolean).
# Важность для анализа: `Высокая` – важно при анализе контрактов, выделяемых в поддержку женского бизнеса.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned": "\n                "

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isMinorityOwned": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isMinorityOwned
# Описание: Указывает, является ли компания бизнесом, принадлежащим представителю меньшинства.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для анализа контракта в контексте поддержки меньшинств.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isSubContinentAsianAmericanOwnedBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isSubContinentAsianAmericanOwnedBusiness
# Описание: Указывает, принадлежит ли компания бизнесу, управляемому американцами из Южной Азии.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для поддержания равенства возможностей для бизнеса.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isAsianPacificAmericanOwnedBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isAsianPacificAmericanOwnedBusiness
# Описание: Указывает, принадлежит ли компания бизнесу, управляемому американцами азиатского и тихоокеанского происхождения.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – поддержка азиатских и тихоокеанских американцев.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isBlackAmericanOwnedBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isBlackAmericanOwnedBusiness
# Описание: Указывает, принадлежит ли компания бизнесу, управляемому чернокожими американцами.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для анализа контрактов, поддерживающих чернокожий бизнес.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isHispanicAmericanOwnedBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isHispanicAmericanOwnedBusiness
# Описание: Указывает, принадлежит ли компания бизнесу, управляемому американцами латинского происхождения.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для анализа контрактов, поддерживающих латинский бизнес.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isNativeAmericanOwnedBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isNativeAmericanOwnedBusiness
# Описание: Указывает, принадлежит ли компания бизнесу, управляемому коренными американцами.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для анализа контрактов, поддерживающих коренные американцы.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isOtherMinorityOwned": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isOtherMinorityOwned
# Описание: Указывает, принадлежит ли компания другому бизнесу, управляемому представителем меньшинства.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для включения других групп меньшинств.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isVerySmallBusiness": "false"
# Переменная: `is_very_small_business`
# Описание: Указывает, является ли компания очень малым бизнесом.
# Формат: Булево (Boolean).
# Важность для анализа: `Высокая` – важно для анализа контрактов, направленных на поддержку очень малого бизнеса.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isWomenOwnedSmallBusiness": "false"
# Переменная: `is_women_owned_small_business`
# Описание: Указывает, принадлежит ли компания малому бизнесу, управляемому женщиной.
# Формат: Булево (Boolean).
# Важность для анализа: `Высокая` – важный индикатор для контрактов, поддерживающих женский малый бизнес.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isEconomicallyDisadvantagedWomenOwnedSmallBusiness": "false"
# Переменная: `is_economically_disadvantaged_women_owned_small_business`
# Описание: Указывает, принадлежит ли компания экономически обездоленной женщине, владеющей малым бизнесом.
# Формат: Булево (Boolean).
# Важность для анализа: `Высокая` – важное поле для анализа поддержки экономически обездоленных женщин.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isJointVentureWomenOwnedSmallBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isJointVentureWomenOwnedSmallBusiness
# Описание: Указывает, является ли компания совместным предприятием, управляемым женщинами.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для понимания структуры совместных предприятий с участием женщин.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isJointVentureEconomicallyDisadvantagedWomenOwnedSmallBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isJointVentureEconomicallyDisadvantagedWomenOwnedSmallBusiness
# Описание: Указывает, является ли компания совместным предприятием, управляемым экономически обездоленными женщинами.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для анализа поддержки совместных предприятий, принадлежащих экономически обездоленным женщинам.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes": "\n              "

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__isCommunityDevelopedCorporationOwnedFirm": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__isCommunityDevelopedCorporationOwnedFirm
# Описание: Указывает, является ли компания корпорацией, принадлежащей развивающемуся сообществу.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для анализа контрактов, поддерживающих развивающиеся сообщества.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__isLaborSurplusAreaFirm": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__isLaborSurplusAreaFirm
# Описание: Указывает, является ли компания фирмой, расположенной в районе с избытком рабочей силы.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для контрактов, направленных на поддержку районов с высоким уровнем безработицы.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__federalGovernment": "\n                "

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__federalGovernment__isFederalGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__federalGovernment__isFederalGovernment
# Описание: Указывает, является ли поставщик федеральным правительственным агентством.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для различения государственных и частных поставщиков.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__federalGovernment__isFederallyFundedResearchAndDevelopmentCorp": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__federalGovernment__isFederallyFundedResearchAndDevelopmentCorp
# Описание: Указывает, является ли поставщик корпорацией, финансируемой федеральным правительством для исследований и разработок.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для контрактов, связанных с государственными исследовательскими корпорациями.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__federalGovernment__isFederalGovernmentAgency": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__federalGovernment__isFederalGovernmentAgency
# Описание: Указывает, является ли поставщик федеральным государственным агентством.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – помогает различать частные компании и государственные учреждения.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__isStateGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__isStateGovernment
# Описание: Указывает, является ли поставщик государственным учреждением на уровне штата.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для контрактов, которые могут быть выделены государственным учреждениям штатов.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment": "\n"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment
# Описание: Контейнер для информации о том, является ли поставщик местным государственным учреждением.
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – само поле не несёт данных, но вложенные элементы полезны.              ",
"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isLocalGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isLocalGovernment
# Описание: Указывает, является ли поставщик местным государственным учреждением (например, городом или округом).
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для различения местных государственных организаций от частных компаний.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isCityLocalGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isCityLocalGovernment
# Описание: Указывает, является ли поставщик местным государственным учреждением на уровне города.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – помогает идентифицировать компании, работающие с городскими властями.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isCountyLocalGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isCountyLocalGovernment
# Описание: Указывает, является ли поставщик местным государственным учреждением на уровне округа.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для анализа контрактов с округами.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isInterMunicipalLocalGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isInterMunicipalLocalGovernment
# Описание: Указывает, является ли поставщик межмуниципальным местным правительственным учреждением.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – может быть полезно для контрактов, направленных на межмуниципальное сотрудничество.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isLocalGovernmentOwned": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isLocalGovernmentOwned
# Описание: Указывает, является ли поставщик учреждением, принадлежащим местному правительству.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для определения собственности на местном уровне.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isMunicipalityLocalGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isMunicipalityLocalGovernment
# Описание: Указывает, является ли поставщик муниципальным местным государственным учреждением.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для определения роли компании в муниципальном управлении.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isSchoolDistrictLocalGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isSchoolDistrictLocalGovernment
# Описание: Указывает, является ли поставщик частью местного школьного округа.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для контрактов, связанных с образованием на местном уровне.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isTownshipLocalGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isTownshipLocalGovernment
# Описание: Указывает, является ли поставщик частью местного правительства на уровне поселений (township).
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для различения поставщиков, работающих на уровне малых населённых пунктов.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__isTribalGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__isTribalGovernment
# Описание: Указывает, является ли поставщик частью племенного правительства.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для поддержки контрактов с племенными организациями.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__isForeignGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__isForeignGovernment
# Описание: Указывает, является ли поставщик иностранным государственным учреждением.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для определения поставщиков, связанных с правительствами других стран.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType": "\n                "

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isCorporateEntityNotTaxExempt": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isCorporateEntityNotTaxExempt
# Описание: Указывает, является ли организация корпоративным предприятием, не освобождённым от налогов.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для различения налоговых категорий организаций.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isCorporateEntityTaxExempt": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isCorporateEntityTaxExempt
# Описание: Указывает, является ли организация корпоративным предприятием, освобождённым от налогов.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для анализа налогового статуса организации.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isPartnershipOrLimitedLiabilityPartnership": "true"
# Переменная: `is_partnership_or_limited_liability_partnership`
# Описание: Указывает, является ли организация партнёрством или партнёрством с ограниченной ответственностью.
# Формат: Булево (Boolean).
# Важность для анализа: `Высокая` – важно для определения типа организации и юридической структуры бизнеса.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isSolePropreitorship": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isSolePropreitorship
# Описание: Указывает, является ли организация индивидуальным предпринимателем.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для определения типа юридической структуры бизнеса.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isSmallAgriculturalCooperative": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isSmallAgriculturalCooperative
# Описание: Указывает, является ли организация малой сельскохозяйственной кооперативной организацией.
# Формат: Булево (Boolean).
# Важность для анализа: Низкая – полезно для специфичных типов контрактов, связанных с сельским хозяйством.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isInternationalOrganization": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isInternationalOrganization
# Описание: Указывает, является ли организация международной.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для определения участия международных организаций в контрактах.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isUSGovernmentEntity": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isUSGovernmentEntity
# Описание: Указывает, является ли организация федеральным правительственным учреждением США.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для анализа контрактов с федеральными правительственными учреждениями США.

"content__award__vendor__vendorSiteDetails__vendorLineOfBusiness": "\n              "

"content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isCommunityDevelopmentCorporation": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isCommunityDevelopmentCorporation
# Описание: Указывает, является ли организация корпорацией, занимающейся развитием сообществ.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для поддержки корпораций, занимающихся развитием местных сообществ.

"content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isDomesticShelter": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isDomesticShelter
# Описание: Указывает, является ли организация приютом для людей в стране.
# Формат: Булево (Boolean).
# Важность для анализа: Низкая – полезно для анализа контрактов, связанных с социальной поддержкой.

"content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isEducationalInstitution": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isEducationalInstitution
# Описание: Указывает, является ли организация образовательным учреждением.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для контрактов с учебными заведениями.

"content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isFoundation": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isFoundation
# Описание: Указывает, является ли организация фондом.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для определения организаций, работающих в сфере благотворительности.

"content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isHospital": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isHospital
# Описание: Указывает, является ли организация больницей.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для контрактов в сфере здравоохранения.

"content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isManufacturerOfGoods": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isManufacturerOfGoods
# Описание: Указывает, является ли организация производителем товаров.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для контрактов, связанных с производственными компаниями.

"content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isVeterinaryHospital": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isVeterinaryHospital
# Описание: Указывает, является ли организация ветеринарной больницей.
# Формат: Булево (Boolean).
# Важность для анализа: Низкая – полезно для контрактов в области ветеринарии.

"content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isHispanicServicingInstitution": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isHispanicServicingInstitution
# Описание: Указывает, является ли организация учреждением, обслуживающим Латиноамериканское сообщество.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для контрактов, направленных на поддержку латиноамериканских организаций.

"content__award__vendor__vendorSiteDetails__vendorRelationshipWithFederalGovernment": "\n              "

"content__award__vendor__vendorSiteDetails__vendorRelationshipWithFederalGovernment__receivesContracts": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorRelationshipWithFederalGovernment__receivesContracts
# Описание: Указывает, получает ли организация контракты от федерального правительства.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для анализа участия в федеральных тендерах.

"content__award__vendor__vendorSiteDetails__vendorRelationshipWithFederalGovernment__receivesGrants": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorRelationshipWithFederalGovernment__receivesGrants
# Описание: Указывает, получает ли организация гранты от федерального правительства.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для понимания, поддерживается ли организация федеральными грантами.

"content__award__vendor__vendorSiteDetails__vendorRelationshipWithFederalGovernment__receivesContractsAndGrants": "true"
# Переменная: `receives_contracts_and_grants`
# Описание: Указывает, получает ли организация как контракты, так и гранты от федерального правительства.
# Формат: Булево (Boolean).
# Важность для анализа: `Высокая` – важный индикатор для анализа поддержки со стороны федеральных органов.

"content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity": "\n              "
# Переменная: content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity
# Описание: Контейнер для информации о типе государственного учреждения.
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – не несёт данных само по себе, но вложенные элементы полезны.

"content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isAirportAuthority": "false"
# Переменная: content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isAirportAuthority
# Описание: Указывает, является ли организация органом власти аэропорта.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для различения организаций, работающих в авиационной сфере.

"content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isCouncilOfGovernments": "false"
# Переменная: content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isCouncilOfGovernments
# Описание: Указывает, является ли организация советом местных органов власти.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – помогает идентифицировать местные или межрегиональные органы власти.

"content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isHousingAuthoritiesPublicOrTribal": "false"
# Переменная: content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isHousingAuthoritiesPublicOrTribal
# Описание: Указывает, является ли организация государственным или племенным жилищным органом.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для анализа контракта с жилищными властями.

"content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isInterstateEntity": "false"
# Переменная: content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isInterstateEntity
# Описание: Указывает, является ли организация межгосударственным органом.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для анализа организаций, работающих между несколькими штатами.

"content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isPlanningCommission": "false"
# Переменная: content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isPlanningCommission
# Описание: Указывает, является ли организация комиссией по планированию.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – помогает понять, работает ли организация в сфере городского или регионального планирования.

"content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isPortAuthority": "false"
# Переменная: content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isPortAuthority
# Описание: Указывает, является ли организация портовой властью.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для анализа работы с портами и морской логистикой.

"content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isTransitAuthority": "false"
# Переменная: content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isTransitAuthority
# Описание: Указывает, является ли организация транспортной властью.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для анализа контракта с транспортными и железнодорожными властями.

"content__award__vendor__vendorSiteDetails__vendorOrganizationFactors": "\n              "

"content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__isSubchapterSCorporation": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__isSubchapterSCorporation
# Описание: Указывает, является ли организация корпорацией по подглаве С (для налоговых целей в США).
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для определения налогового статуса компании.

"content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__isLimitedLiabilityCorporation": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__isLimitedLiabilityCorporation
# Описание: Указывает, является ли организация ограниченной ответственностью (LLC).
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – помогает различить организационные формы компаний.

"content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__isForeignOwnedAndLocated": "true"
# Переменная: content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__isForeignOwnedAndLocated
# Описание: Указывает, является ли организация иностранной, как по собственности, так и по расположению.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для анализа контрактов с иностранными компаниями.

"content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__profitStructure": "\n                "

"content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__profitStructure__isForProfitOrganization": "true"
# Переменная: `is_for_profit_organization`
# Описание: Указывает, является ли организация коммерческой, целью которой является получение прибыли.
# Формат: Булево (Boolean).
# Важность для анализа: `Высокая` – важно для анализа коммерческих организаций.

"content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__profitStructure__isNonprofitOrganization": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__profitStructure__isNonprofitOrganization
# Описание: Указывает, является ли организация некоммерческой.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для анализа контрактов с некоммерческими организациями.

"content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__profitStructure__isOtherNotForProfitOrganization": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__profitStructure__isOtherNotForProfitOrganization
# Описание: Указывает, является ли организация другой некоммерческой организацией.
# Формат: Булево (Boolean).
# Важность для анализа: Низкая – важно для разнообразных типов некоммерческих организаций.

"content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__isShelteredWorkshop": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__isShelteredWorkshop
# Описание: Указывает, является ли организация защищённым предприятием для инвалидов.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для поддержки контрактов с организациями, поддерживающими инвалидов.

"content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__stateOfIncorporation": "DE"
# Переменная: `vendor_state_of_incorporation`
# Описание: Указывает штат, в котором зарегистрирована организация.
# Формат: Строка (String), например, "DE", что означает штат Делавэр.
# Важность для анализа: `Высокая` – важно для определения местоположения и юридической юрисдикции компании.

"content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__stateOfIncorporation__name": "DELAWARE"
# Переменная: content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__stateOfIncorporation__name
# Описание: Название штата, в котором зарегистрирована организация (в данном случае, Делавэр).
# Формат: Строка (String), например, "DELAWARE".
# Важность для анализа: Средняя – полезно для понимания юрисдикции регистрации бизнеса, особенно в контексте юридических требований.

"content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__countryOfIncorporation": "USA"
# Переменная: `vendor_country_of_incorporation`
# Описание: Указывает страну, в которой зарегистрирована организация.
# Формат: Строка (String), например, "USA", что означает США.
# Важность для анализа: `Высокая` – важно для различения местных и иностранных компаний.

"content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__countryOfIncorporation__name": "UNITED STATES"
# Переменная: content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__countryOfIncorporation__name
# Описание: Полное название страны, в которой зарегистрирована организация (в данном случае, США).
# Формат: Строка (String), например, "UNITED STATES".
# Важность для анализа: Средняя – помогает различать компании, зарегистрированные в США, и за рубежом.

"content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__organizationalType": "PARTNERSHIP"
# Переменная: content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__organizationalType
# Описание: Указывает тип организационной формы бизнеса (например, партнёрство).
# Формат: Строка (String), например, "PARTNERSHIP", что означает партнёрство.
# Важность для анализа: Средняя – помогает определить юридическую структуру организации.

"content__award__vendor__vendorSiteDetails__typeOfEducationalEntity": "\n              "

"content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__is1862LandGrantCollege": "false"
# Переменная: content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__is1862LandGrantCollege
# Описание: Указывает, является ли организация университетом, основанным по закону 1862 года (Land Grant College).
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для анализа контрактов с учебными заведениями, получившими землю по закону 1862 года.

"content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__is1890LandGrantCollege": "false"
# Переменная: content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__is1890LandGrantCollege
# Описание: Указывает, является ли организация университетом, основанным по закону 1890 года (Land Grant College).
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для анализа контрактов с университетами, основанными по закону 1890 года.

"content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__is1994LandGrantCollege": "false"
# Переменная: content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__is1994LandGrantCollege
# Описание: Указывает, является ли организация университетом, основанным по закону 1994 года (Land Grant College).
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для анализа контрактов с университетами, основанными по закону 1994 года.

"content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isHistoricallyBlackCollegeOrUniversity": "false"
# Переменная: content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isHistoricallyBlackCollegeOrUniversity
# Описание: Указывает, является ли организация исторически черным колледжем или университетом.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для анализа контрактов с исторически черными колледжами или университетами.

"content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isMinorityInstitution": "false"
# Переменная: content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isMinorityInstitution
# Описание: Указывает, является ли организация учебным заведением, обслуживающим меньшинства.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для анализа контрактов с учреждениями, поддерживающими образовательные возможности для меньшинств.

"content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isPrivateUniversityOrCollege": "false"
# Переменная: content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isPrivateUniversityOrCollege
# Описание: Указывает, является ли организация частным университетом или колледжем.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для различения частных и государственных образовательных учреждений.

"content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isSchoolOfForestry": "false"
# Переменная: content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isSchoolOfForestry
# Описание: Указывает, является ли организация школой лесного хозяйства.
# Формат: Булево (Boolean).
# Важность для анализа: Низкая – полезно для контрактов, связанных с лесным хозяйством.

"content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isStateControlledInstitutionofHigherLearning": "false"
# Переменная: content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isStateControlledInstitutionofHigherLearning
# Описание: Указывает, является ли организация государственным учреждением высшего образования.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для анализа контрактов с государственными университетами.

"content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isTribalCollege": "false"
# Переменная: content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isTribalCollege
# Описание: Указывает, является ли организация племенным колледжем.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для анализа контрактов с племенными образовательными учреждениями.

"content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isVeterinaryCollege": "false"
# Переменная: content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isVeterinaryCollege
# Описание: Указывает, является ли организация ветеринарным колледжем.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для контрактов, связанных с ветеринарным образованием.

"content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isAlaskanNativeServicingInstitution": "false"
# Переменная: content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isAlaskanNativeServicingInstitution
# Описание: Указывает, является ли организация учреждением, обслуживающим коренных жителей Аляски.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для контрактов с учреждениями, поддерживающими коренных жителей Аляски.

"content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isNativeHawaiianServicingInstitution": "false"
# Переменная: content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isNativeHawaiianServicingInstitution
# Описание: Указывает, является ли организация учреждением, обслуживающим коренных гавайцев.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для контрактов с учреждениями, поддерживающими коренных гавайцев.

"content__award__vendor__vendorSiteDetails__vendorCertifications": "\n              "

"content__award__vendor__vendorSiteDetails__vendorCertifications__isDOTCertifiedDisadvantagedBusinessEnterprise": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorCertifications__isDOTCertifiedDisadvantagedBusinessEnterprise
# Описание: Указывает, сертифицирована ли организация как предприятие с ограниченными возможностями, сертифицированное Министерством транспорта США.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для анализа контрактов с предприятиями, сертифицированными по программе DOT.

"content__award__vendor__vendorSiteDetails__vendorCertifications__isSelfCertifiedSmallDisadvantagedBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorCertifications__isSelfCertifiedSmallDisadvantagedBusiness
# Описание: Указывает, является ли организация малым предприятием, самостоятельно сертифицированным как предприятие с ограниченными возможностями.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для анализа контрактов с малыми предприятиями с ограниченными возможностями.

"content__award__vendor__vendorSiteDetails__vendorCertifications__isSBACertifiedSmallDisadvantagedBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorCertifications__isSBACertifiedSmallDisadvantagedBusiness
# Описание: Указывает, сертифицировано ли малое предприятие как предприятие с ограниченными возможностями по программе SBA.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – важно для анализа контрактов с сертифицированными малыми предприятиями.

"content__award__vendor__vendorSiteDetails__vendorCertifications__isSBACertified8AProgramParticipant": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorCertifications__isSBACertified8AProgramParticipant
# Описание: Указывает, является ли организация участником программы SBA 8(a) (для малых предприятий).
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для анализа контрактов с организациями, участвующими в программе 8(a).

"content__award__vendor__vendorSiteDetails__vendorCertifications__isSelfCertifiedHUBZoneJointVenture": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorCertifications__isSelfCertifiedHUBZoneJointVenture
# Описание: Указывает, является ли организация совместным предприятием, самостоятельно сертифицированным по программе HUBZone.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для анализа совместных предприятий в рамках программы HUBZone.

"content__award__vendor__vendorSiteDetails__vendorCertifications__isSBACertifiedHUBZone": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorCertifications__isSBACertifiedHUBZone
# Описание: Указывает, сертифицирована ли организация в качестве малого бизнеса в зоне разработки HUBZone.
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для анализа контрактов с организациями в рамках программы HUBZone.

"content__award__vendor__vendorSiteDetails__vendorCertifications__isSBACertified8AJointVenture": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorCertifications__isSBACertified8AJointVenture
# Описание: Указывает, является ли организация совместным предприятием, сертифицированным в рамках программы SBA 8(a).
# Формат: Булево (Boolean).
# Важность для анализа: Средняя – полезно для анализа совместных предприятий, сертифицированных в рамках SBA 8(a).

"content__award__vendor__vendorSiteDetails__vendorLocation": "\n              "

"content__award__vendor__vendorSiteDetails__vendorLocation__streetAddress": "3737 MARSHALL AVE"
# Переменная: `vendor_location_street_address`
# Описание: Улица, на которой расположена организация.
# Формат: Строка (String), например, "3737 MARSHALL AVE".
# Важность для анализа: `Высокая` – полезно для точного определения местоположения поставщика.

"content__award__vendor__vendorSiteDetails__vendorLocation__city": "SAINT LOUIS"
# Переменная: `vendor_location_city`
# Описание: Город, в котором расположена организация.
# Формат: Строка (String), например, "SAINT LOUIS".
# Важность для анализа: `Высокая` – полезно для географической идентификации поставщика.

"content__award__vendor__vendorSiteDetails__vendorLocation__state": "MO"
# Переменная: `vendor_location_state`
# Описание: Код штата, в котором расположена организация.
# Формат: Строка (String), например, "MO", что означает штат Миссури.
# Важность для анализа: `Высокая` – полезно для определения местоположения в рамках США.

"content__award__vendor__vendorSiteDetails__vendorLocation__state__name": "MISSOURI"
# Переменная: content__award__vendor__vendorSiteDetails__vendorLocation__state__name
# Описание: Полное название штата, в котором расположена организация.
# Формат: Строка (String), например, "MISSOURI".
# Важность для анализа: Средняя – полезно для полной идентификации местоположения.

"content__award__vendor__vendorSiteDetails__vendorLocation__ZIPCode": "63119"
# Переменная: `vendor_location_zipcode`
# Описание: Почтовый индекс местоположения организации.
# Формат: Строка (String), например, "63119".
# Важность для анализа: `Высокая` – полезно для точной географической локализации.

"content__award__vendor__vendorSiteDetails__vendorLocation__ZIPCode__city": "SAINT LOUIS"
# Переменная: content__award__vendor__vendorSiteDetails__vendorLocation__ZIPCode__city
# Описание: Город, соответствующий почтовому индексу.
# Формат: Строка (String), например, "SAINT LOUIS".
# Важность для анализа: Средняя – полезно для подтверждения города, связанного с почтовым индексом.

"content__award__vendor__vendorSiteDetails__vendorLocation__countryCode": "USA"
# Переменная: `vendor_location_country`
# Описание: Код страны, в которой расположена организация.
# Формат: Строка (String), например, "USA", что означает США.
# Важность для анализа: `Высокая` – важно для международной идентификации поставщика.

"content__award__vendor__vendorSiteDetails__vendorLocation__countryCode__name": "UNITED STATES"
# Переменная: content__award__vendor__vendorSiteDetails__vendorLocation__countryCode__name
# Описание: Полное название страны, в которой расположена организация.
# Формат: Строка (String), например, "UNITED STATES".
# Важность для анализа: Средняя – дублирует 'content__award__vendor__vendorSiteDetails__vendorLocation__countryCode' полезно для подтверждения страны происхождения.

"content__award__vendor__vendorSiteDetails__vendorLocation__phoneNo": "9204618790"
# Переменная: content__award__vendor__vendorSiteDetails__vendorLocation__phoneNo
# Описание: Номер телефона организации.
# Формат: Строка (String), например, "9204618790".
# Важность для анализа: Средняя – полезно для связи с поставщиком.

"content__award__vendor__vendorSiteDetails__vendorLocation__congressionalDistrictCode": "02"
# Переменная: content__award__vendor__vendorSiteDetails__vendorLocation__congressionalDistrictCode
# Описание: Код конгрессного округа, в котором расположена организация.
# Формат: Строка (String), например, "02".
# Важность для анализа: Средняя – полезно для анализа, в каком округе находится организация для политической или налоговой идентификации.

"content__award__vendor__vendorSiteDetails__vendorLocation__entityDataSource": "D&B"
# Переменная: content__award__vendor__vendorSiteDetails__vendorLocation__entityDataSource
# Описание: Источник данных об организации (например, Dun & Bradstreet).
# Формат: Строка (String), например, "D&B".
# Важность для анализа: Низкая – полезно для проверки достоверности данных о поставщике.

"content__award__vendor__vendorSiteDetails__vendorLocation__vendorAlternateSiteCode": "63119"
# Переменная: content__award__vendor__vendorSiteDetails__vendorLocation__vendorAlternateSiteCode
# Описание: Альтернативный код местоположения, связанный с организацией.
# Формат: Строка (String), например, "63119".
# Важность для анализа: Низкая – может быть полезно для уточнения местоположения или идентификации альтернативных адресов.

"content__award__vendor__vendorSiteDetails__entityIdentifiers": "\n              "
"content__award__vendor__vendorSiteDetails__entityIdentifiers__vendorUEIInformation": "\n                "

"content__award__vendor__vendorSiteDetails__entityIdentifiers__vendorUEIInformation__UEI": "QGUQWSU5AHB4"
# Переменная: `vendor_uei`
# Описание: Уникальный идентификатор организации (UEI), используемый для официальной идентификации.
# Формат: Строка (String).
# Важность для анализа: `Высокая` – важно для точной идентификации юридического лица в государственных контрактах.

"content__award__vendor__vendorSiteDetails__entityIdentifiers__vendorUEIInformation__UEILegalBusinessName": "PERIMETER SOLUTIONS LP"
# Переменная: content__award__vendor__vendorSiteDetails__entityIdentifiers__vendorUEIInformation__UEILegalBusinessName
# Описание: Юридическое название организации, соответствующее её Unique Entity Identifier.
# Формат: Строка (String), например, "PERIMETER SOLUTIONS LP".
# Важность для анализа: Средняя – полезно для подтверждения легальности и правильности наименования организации.

"content__award__vendor__vendorSiteDetails__entityIdentifiers__vendorUEIInformation__ultimateParentUEI": "LBLLJKAVKL68"
# Переменная: `vendor_ultimate_parent_uei`
# Описание: UEI основного (родительского) бизнеса или организации, которая является владельцем или управляющим.
# Формат: Строка (String).
# Важность для анализа: `Высокая` – полезно для понимания структуры владения и управления.

"content__award__vendor__vendorSiteDetails__entityIdentifiers__vendorUEIInformation__ultimateParentUEIName": "PERIMETER SOLUTIONS LP"
# Переменная: content__award__vendor__vendorSiteDetails__entityIdentifiers__vendorUEIInformation__ultimateParentUEIName
# Описание: Название организации, являющейся владельцем или управляющим организацией (родитель).
# Формат: Строка (String).
# Важность для анализа: Средняя – помогает понять, кто является владельцем или управляющим организацией.

"content__award__vendor__vendorSiteDetails__entityIdentifiers__cageCode": "1RKV8"
# Переменная: `vendor_cage_code`
# Описание: CAGE (Commercial and Government Entity) код, присвоенный организации для государственных контрактов.
# Формат: Строка (String).
# Важность для анализа: `Высокая` – важно для точной идентификации организации в контрактных и государственных документах.

"content__award__vendor__vendorSiteDetails__ccrRegistrationDetails": "\n              "

"content__award__vendor__vendorSiteDetails__ccrRegistrationDetails__registrationDate": "2000-09-16 00:00:00"
# Переменная: `vendor_registration_date`
# Описание: Дата регистрации организации в CCR.
# Формат: Дата и время (DateTime).
# Важность для анализа: `Высокая` – полезно для понимания того, как долго организация зарегистрирована в системе.

"content__award__vendor__vendorSiteDetails__ccrRegistrationDetails__renewalDate": "2019-05-24 00:00:00"
# Переменная: `vendor_renewal_date`
# Описание: Дата продления регистрации организации в CCR.
# Формат: Дата и время (DateTime), например, "2019-05-24 00:00:00".
# Важность для анализа: `Высокая` – помогает понять актуальность регистрации организации в CCR.

"content__award__vendor__contractingOfficerBusinessSizeDetermination": "O"
# Переменная: `vendor_size`
# Описание: Оценка размера бизнеса, произведённая контрактующим офицером.
# Формат: Строка (String).
# Важность для анализа: `Высокая` – полезно для понимания размера бизнеса и его классификации.

"content__award__vendor__contractingOfficerBusinessSizeDetermination__description": "OTHER THAN SMALL BUSINESS"
# Переменная: content__award__vendor__contractingOfficerBusinessSizeDetermination__description
# Описание: Описание оценки размера бизнеса, произведённой контрактующим офицером.
# Формат: Строка (String), например, "OTHER THAN SMALL BUSINESS".
# Важность для анализа: Средняя – важно для определения статуса бизнеса в контексте государственных контрактов.

"content__award__placeOfPerformance": "\n          "
"content__award__placeOfPerformance__principalPlaceOfPerformance": "\n            "

"content__award__placeOfPerformance__principalPlaceOfPerformance__stateCode": "ID"
# Переменная: `place_of_performance_state`
# Описание: Код штата, в котором выполняется контракт.
# Формат: Строка (String), например, "ID", что означает штат Айдахо.
# Важность для анализа: `Высокая` – важно для точной географической локализации исполнения контракта.

"content__award__placeOfPerformance__principalPlaceOfPerformance__stateCode__name": "IDAHO"
# Переменная: content__award__placeOfPerformance__principalPlaceOfPerformance__stateCode__name
# Описание: Название штата, в котором выполняется контракт.
# Формат: Строка (String), например, "IDAHO".
# Важность для анализа: Средняя – дублирует 'content__award__placeOfPerformance__principalPlaceOfPerformance__stateCode' полезно для полной идентификации местоположения контракта.

"content__award__placeOfPerformance__principalPlaceOfPerformance__countryCode": "USA"
# Переменная: `place_of_performance_country`
# Описание: Код страны, в которой выполняется контракт.
# Формат: Строка (String), например, "USA", что означает США.
# Важность для анализа: `Высокая` – важно для понимания, в какой стране исполняется контракт.

"content__award__placeOfPerformance__principalPlaceOfPerformance__countryCode__name": "UNITED STATES"
# Переменная: content__award__placeOfPerformance__principalPlaceOfPerformance__countryCode__name
# Описание: Полное название страны, в которой выполняется контракт.
# Формат: Строка (String), например, "UNITED STATES".
# Важность для анализа: Средняя – помогает в точной идентификации страны исполнения контракта.

"content__award__placeOfPerformance__placeOfPerformanceZIPCode": "837055354"
# Переменная: `place_of_performance_zip`
# Описание: Почтовый индекс места исполнения контракта.
# Формат: Строка (String), например, "837055354".
# Важность для анализа: `Высокая` – полезно для точной географической локализации контракта.

"content__award__placeOfPerformance__placeOfPerformanceZIPCode__county": "ADA"
# Переменная: content__award__placeOfPerformance__placeOfPerformanceZIPCode__county
# Описание: Округ, соответствующий почтовому индексу места исполнения контракта.
# Формат: Строка (String), например, "ADA".
# Важность для анализа: Средняя – полезно для уточнения географического местоположения.

"content__award__placeOfPerformance__placeOfPerformanceZIPCode__city": "BOISE"
# Переменная: content__award__placeOfPerformance__placeOfPerformanceZIPCode__city
# Описание: Город, соответствующий почтовому индексу места исполнения контракта.
# Формат: Строка (String), например, "BOISE".
# Важность для анализа: Средняя – полезно для точного определения города исполнения контракта.

"content__award__placeOfPerformance__placeOfPerformanceCongressionalDistrict": "01"
# Переменная: content__award__placeOfPerformance__placeOfPerformanceCongressionalDistrict
# Описание: Код конгрессного округа, в котором исполняется контракт.
# Формат: Строка (String), например, "01".
# Важность для анализа: Средняя – полезно для определения политического округа, что может быть важно для анализа государственной деятельности.

"content__award__competition": "\n          "

"content__award__competition__extentCompeted": "C"
# Переменная: `competition_extent_competed`
# Описание: Уровень конкуренции по контракту.
# Формат: Строка (String), например, "C", что может означать "NOT COMPETED" (не было конкуренции).
# Важность для анализа: `Высокая` – помогает понять, была ли конкуренция на контракт или он был предоставлен без конкуренции.

"content__award__competition__extentCompeted__description": "NOT COMPETED"
# Переменная: content__award__competition__extentCompeted__description
# Описание: Описание уровня конкуренции.
# Формат: Строка (String), например, "NOT COMPETED".
# Важность для анализа: Средняя – важно для понимания, был ли контракт конкурентным или не было других предложений.

"content__award__competition__solicitationProcedures": "SSS"
# Переменная: `competition_solicitation_procedures`
# Описание: Процедура подачи предложений для контракта.
# Формат: Строка (String), например, "SSS", что может означать "ONLY ONE SOURCE" (только один источник).
# Важность для анализа: `Высокая` – помогает определить, использовалась ли процедура запросов предложений для контракта.

"content__award__competition__solicitationProcedures__description": "ONLY ONE SOURCE"
# Переменная: content__award__competition__solicitationProcedures__description
# Описание: Описание процедуры подачи предложений.
# Формат: Строка (String), например, "ONLY ONE SOURCE".
# Важность для анализа: Средняя – важно для понимания, был ли контракт ограничен одним источником.

"content__award__competition__idvTypeOfSetAside": "NONE"
# Переменная: content__award__competition__idvTypeOfSetAside
# Описание: Указывает, был ли применён тип выделенного контракта для малых или других компаний.
# Формат: Строка (String), например, "NONE", что означает отсутствие выделения.
# Важность для анализа: Средняя – полезно для понимания, были ли какие-либо выделения для определённых типов организаций.

"content__award__competition__idvTypeOfSetAside__description": "NO SET ASIDE USED."
# Переменная: content__award__competition__idvTypeOfSetAside__description
# Описание: Описание того, использовался ли тип выделенного контракта.
# Формат: Строка (String), например, "NO SET ASIDE USED.".
# Важность для анализа: Средняя – полезно для понимания, было ли исключение для определённой категории бизнеса.

"content__award__competition__typeOfSetAsideSource": "B"
# Переменная: content__award__competition__typeOfSetAsideSource
# Описание: Источник для выделения контракта.
# Формат: Строка (String), например, "B", что может означать "IDC" (Indefinite Delivery Contract – бессрочный контракт).
# Важность для анализа: Средняя – полезно для анализа источников выделений контрактов.

"content__award__competition__typeOfSetAsideSource__description": "IDC"
# Переменная: content__award__competition__typeOfSetAsideSource__description
# Описание: Описание источника для выделения контракта.
# Формат: Строка (String), например, "IDC", что означает бессрочный контракт.
# Важность для анализа: Средняя – полезно для понимания, на какой основе был выделен контракт.

"content__award__competition__evaluatedPreference": "NONE"
# Переменная: content__award__competition__evaluatedPreference
# Описание: Указывает, был ли использован предпочтительный анализ при оценке предложений.
# Формат: Строка (String), например, "NONE", что означает отсутствие предпочтений.
# Важность для анализа: Средняя – полезно для анализа, использовались ли какие-либо предпочтения при оценке контрактов.

"content__award__competition__evaluatedPreference__description": "NO PREFERENCE USED"
# Переменная: content__award__competition__evaluatedPreference__description
# Описание: Описание предпочтений, если таковые были.
# Формат: Строка (String), например, "NO PREFERENCE USED".
# Важность для анализа: Средняя – важно для понимания, был ли контракт оценён без предпочтений или с ними.

"content__award__competition__reasonNotCompeted": "ONE"
# Переменная: `competition_reason_not_competed`
# Описание: Причина, по которой контракт не был конкурентным.
# Формат: Строка (String), например, "ONE", что может означать, что был только один участник.
# Важность для анализа: `Высокая` – важно для анализа, почему не было конкуренции и почему контракт был предоставлен без конкурентных предложений.

"content__award__competition__reasonNotCompeted__description": "ONLY ONE SOURCE-OTHER (FAR 6.302-1 OTHER)"
# Переменная: content__award__competition__reasonNotCompeted__description
# Описание: Причина, по которой контракт не был конкурентным, указано "только один источник".
# Формат: Строка (String), например, "ONLY ONE SOURCE-OTHER (FAR 6.302-1 OTHER)".
# Важность для анализа: Средняя – важная информация для понимания причин отсутствия конкуренции и применения специальной исключительной процедуры.

"content__award__competition__idvNumberOfOffersReceived": "1"
# Переменная: `competition_idv_number_of_offers_received`
# Описание: Количество предложений, полученных для контракта.
# Формат: Число (Integer), например, '1'.
# Важность для анализа: `Высокая` – полезно для анализа уровня конкуренции и активности на рынке.

"content__award__competition__numberOfOffersSource": "B"
# Переменная: content__award__competition__numberOfOffersSource
# Описание: Источник предложений для контракта.
# Формат: Строка (String), например, "B", что может означать "IDC" (Indefinite Delivery Contract – бессрочный контракт).
# Важность для анализа: Средняя – полезно для понимания, какой тип контракта был использован и сколько предложений было подано.

"content__award__competition__numberOfOffersSource__description": "IDC"
# Переменная: content__award__competition__numberOfOffersSource__description
# Описание: Описание источника предложений.
# Формат: Строка (String), например, "IDC", что означает бессрочный контракт.
# Важность для анализа: Средняя – помогает понять, как был организован запрос предложений.

"content__award__competition__commercialItemAcquisitionProcedures": "A"
# Переменная: content__award__competition__commercialItemAcquisitionProcedures
# Описание: Указывает, использовалась ли процедура для приобретения коммерческих товаров и услуг.
# Формат: Строка (String), например, "A", что может означать приобретение коммерческих товаров/услуг.
# Важность для анализа: Средняя – полезно для понимания типа контракта и того, как были приобретены товары или услуги.

"content__award__competition__commercialItemAcquisitionProcedures__description": "COMMERCIAL PRODUCTS/SERVICES"
# Переменная: content__award__competition__commercialItemAcquisitionProcedures__description
# Описание: Описание процедуры для приобретения коммерческих товаров и услуг.
# Формат: Строка (String), например, "COMMERCIAL PRODUCTS/SERVICES".
# Важность для анализа: Средняя – помогает понять, что контракт связан с покупкой коммерческих товаров и услуг.

"content__award__competition__commercialItemTestProgram": "N"
# Переменная: content__award__competition__commercialItemTestProgram
# Описание: Указывает, использовалась ли программа тестирования коммерческих товаров.
# Формат: Строка (String)
# Важность для анализа: Низкая – полезно для определения, использовалась ли программа тестирования коммерческих товаров.

"content__award__competition__commercialItemTestProgram__description": "NO"
# Переменная: content__award__competition__commercialItemTestProgram__description
# Описание: Описание того, использовалась ли программа тестирования коммерческих товаров.
# Формат: Строка (String).
# Важность для анализа: Низкая – помогает уточнить, была ли использована программа для тестирования товаров.

"content__award__competition__A76Action": "N"
# Переменная: content__award__competition__A76Action
# Описание: Указывает, был ли применён A-76 процесс для определения того, должны ли государственные учреждения выполнять работу или это можно передать частным подрядчикам.
# Формат: Строка (String).
# Важность для анализа: Средняя – полезно для понимания, использовалась ли государственная программа для определения, следует ли передавать контракт частным компаниям.

"content__award__competition__A76Action__description": "NO"
# Переменная: content__award__competition__A76Action__description
# Описание: Описание того, использовался ли процесс A-76 для контракта.
# Формат: Строка (String).
# Важность для анализа: Средняя – помогает уточнить, применялись ли процедуры, связанные с программой A-76.

"content__award__competition__fedBizOpps": "Y"
# Переменная: `competition_fed_biz_opps`
# Описание: Указывает, были ли сделаны публичные объявления о федеральных бизнес-возможностях (Federal Business Opportunities).
# Формат: Строка (String).
# Важность для анализа: `Высокая` – полезно для анализа доступности контракта для широкого круга поставщиков и прозрачности процесса.

"content__award__competition__fedBizOpps__description": "YES"
# Переменная: content__award__competition__fedBizOpps__description
# Описание: Описание того, были ли сделаны объявления о федеральных бизнес-возможностях.
# Формат: Строка (String).
# Важность для анализа: Средняя – дублирует 'content__award__competition__fedBizOpps' важно для подтверждения, что информация о контракте была доступна публично.

"content__award__competition__localAreaSetAside": "N"
# Переменная: content__award__competition__localAreaSetAside
# Описание: Указывает, был ли применён локальный набор контрактов (например, для местных или малых предприятий).
# Формат: Строка (String).
# Важность для анализа: Средняя – полезно для понимания, был ли контракт ограничен для местных предприятий или поставщиков.

"content__award__competition__localAreaSetAside__description": "NO"
# Переменная: content__award__competition__localAreaSetAside__description
# Описание: Описание того, был ли использован локальный набор для контракта.
# Формат: Строка (String)
# Важность для анализа: Средняя – помогает уточнить, было ли географическое ограничение для получения контракта.

"content__award__preferencePrograms": "\n          "

"content__award__preferencePrograms__subcontractPlan": "G"
# Переменная: content__award__preferencePrograms__subcontractPlan
# Описание: Указывает, используется ли программа для субподрядов, и если используется, то какой тип.
# Формат: Строка (String).
# Важность для анализа: Средняя – важно для понимания, применяется ли коммерческий план для субподрядов в контракте.

"content__award__preferencePrograms__subcontractPlan__description": "COMMERCIAL SUBCONTRACT PLAN"
# Переменная: content__award__preferencePrograms__subcontractPlan__description
# Описание: Описание того, что это за план субподряда.
# Формат: Строка (String).
# Важность для анализа: Средняя – помогает понять, используется ли коммерческий план для субподряда в рамках контракта.

"content__award__transactionInformation": "\n          "

"content__award__transactionInformation__createdBy": "LARRYROBILLARD@FS.FED.US"
# Переменная: content__award__transactionInformation__createdBy
# Описание: Электронная почта пользователя, создавшего транзакцию.
# Формат: Строка (String).
# Важность для анализа: Средняя – полезно для отслеживания, кто инициировал транзакцию.

"content__award__transactionInformation__createdDate": "2023-02-07 14:27:43"
# Переменная: content__award__transactionInformation__createdDate
# Описание: Дата и время создания транзакции.
# Формат: Дата и время (DateTime).
# Важность для анализа: Средняя – полезно для отслеживания, когда была создана транзакция.

"content__award__transactionInformation__lastModifiedBy": "LARRYROBILLARD@FS.FED.US"
# Переменная: content__award__transactionInformation__lastModifiedBy
# Описание: Электронная почта пользователя, последний раз изменившего транзакцию.
# Формат: Строка (String).
# Важность для анализа: Средняя – полезно для отслеживания, кто и когда изменял данные транзакции.

"content__award__transactionInformation__lastModifiedDate": "2023-02-07 15:12:28"
# Переменная: content__award__transactionInformation__lastModifiedDate
# Описание: Дата и время последнего изменения транзакции.
# Формат: Дата и время (DateTime).
# Важность для анализа: Средняя – полезно для отслеживания, когда произошли изменения в транзакции.

"content__award__transactionInformation__status": "F"
# Переменная: `award_transaction_information_status`
# Описание: Статус транзакции.
# Формат: Строка (String).
# Важность для анализа: `Высокая` – важно для понимания текущего состояния транзакции (например, завершена или ожидает).

"content__award__transactionInformation__status__description": "FINAL"
# Переменная: content__award__transactionInformation__status__description
# Описание: Описание статуса транзакции.
# Формат: Строка (String).
# Важность для анализа: Средняя – дублирует 'content__award__transactionInformation__status' важно для понимания, является ли транзакция окончательной.

"content__award__transactionInformation__approvedBy": "LARRYROBILLARD@FS.FED.US"
# Переменная: content__award__transactionInformation__approvedBy
# Описание: Электронная почта пользователя, утвердившего транзакцию.
# Формат:  м
# Важность для анализа: Средняя – полезно для отслеживания, кто утвердил транзакцию.

"content__award__transactionInformation__approvedDate": "2023-02-07 15:12:28"
# Переменная: content__award__transactionInformation__approvedDate
# Описание: Дата и время утверждения транзакции.
# Формат: Дата и время (DateTime).
# Важность для анализа: Средняя – полезно для отслеживания, когда была утверждена транзакция.

"content__award__transactionInformation__closedStatus": "N"
# Переменная: content__award__transactionInformation__closedStatus
# Описание: Указывает, закрыта ли транзакция.
# Формат: Строка (String).
# Важность для анализа: Средняя – полезно для анализа, завершена ли транзакция или нет.

"content__award__genericTags": "\n          "
"content__award__genericTags__genericStrings": "\n            "

"content__award__genericTags__genericStrings__genericString01": "2022-12-29 00:00:00"
# Переменная: content__award__genericTags__genericStrings__genericString01
# Описание: Дата, связанная с контрактом.
# Формат: Дата и время (DateTime).
# Важность для анализа: Средняя – полезно для отслеживания временных рамок, связанных с контрактом.

"content__award__genericTags__genericStrings__genericString02": "QGUQWSU5AHB4"
# Переменная: content__award__genericTags__genericStrings__genericString02
# Описание: Уникальный идентификатор (например, UEI) организации или контракта.
# Формат: Строка (String).
# Важность для анализа: Средняя – теги дополнительной информации.