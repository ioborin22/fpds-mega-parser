"title": "New DELIVERY ORDER 1202SC23K2500 awarded to PERIMETER SOLUTIONS LP for the amount of $5,000,000"
# Переменная: title
# Описание: Краткое текстовое описание контракта.
# Формат: Строка (String).
# Важность для анализа: Низкая – содержит дублирующуюся информацию, которая уже представлена в других полях.
"contract_type": "AWARD"
# Переменная: contract_type
# Описание: Тип контракта (например, AWARD, IDV, OTA).
# Формат: Строка (String).
# Важность для анализа: Высокая – помогает классифицировать контракт по типу.
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
# Переменная: modified
# Описание: Дата и время последнего изменения данных о контракте.
# Формат: Дата и время (YYYY-MM-DD HH:MM:SS).
# Важность для анализа: Средняя – позволяет отслеживать актуальность данных и изменения в контракте.
"content": "\n      "
# Переменная: content
# Описание: Основное содержимое контракта, возможно, включает вложенные данные в формате XML.
# Формат: Строка (String), обычно XML или пустая строка.
# Важность для анализа: Низкая – часто пустое поле или содержит дублируемую информацию, которая уже представлена в других полях.
"content__type": "application/xml"
# Переменная: content__type
# Описание: Указывает формат данных внутри `content`, в данном случае XML.
# Формат: Строка (String).
# Важность для анализа: Низкая – полезно только для определения формата данных, не несёт важной аналитической информации.
"content__award": "\n        "
# Переменная: content__award
# Описание: Контейнер для данных о контракте, содержащий вложенные элементы.
# Формат: Строка (String), обычно XML-структура.
# Важность для анализа: Низкая – само поле не несёт информации, но его вложенные элементы важны.
"content__award__version": "1.5"
# Переменная: content__award__version
# Описание: Версия схемы данных контракта в FPDS.
# Формат: Строка (String).
# Важность для анализа: Низкая – важно только при анализе изменений структуры данных FPDS.
"content__award__awardID": "\n"
# Переменная: content__award__awardID
# Описание: Контейнер для уникального идентификатора награждённого контракта.
# Формат: Строка (String), обычно пустая или содержит вложенные данные.
# Важность для анализа: Низкая – само поле не несёт информации, но вложенные элементы (PIID, Agency ID) важны.
"content__award__awardID__awardContractID": "\n            "
# Переменная: content__award__awardID__awardContractID
# Описание: Контейнер, содержащий информацию о контракте, включая агентство и идентификатор контракта.
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – само поле не несёт информации, но его вложенные элементы важны.
"content__award__awardID__awardContractID__agencyID": "12C2"
# Переменная: content__award__awardID__awardContractID__agencyID
# Описание: Код агентства, заключившего контракт.
# Формат: Строка (String).
# Важность для анализа: Высокая – позволяет определить, какое агентство отвечает за контракт.
"content__award__awardID__awardContractID__agencyID__name": "FOREST SERVICE"
# Переменная: content__award__awardID__awardContractID__agencyID__name
# Описание: Название агентства, заключившего контракт.
# Формат: Строка (String).
# Важность для анализа: Средняя – дублирует `agencyID`, но полезна для удобочитаемости.
"content__award__awardID__awardContractID__PIID": "1202SC23K2500"
# Переменная: content__award__awardID__awardContractID__PIID
# Описание: Уникальный идентификатор контракта (Procurement Instrument Identifier, PIID).
# Формат: Строка (String).
# Важность для анализа: Высокая – основной идентификатор контракта, необходимый для поиска и анализа.
"content__award__awardID__awardContractID__modNumber": "0"
# Переменная: content__award__awardID__awardContractID__modNumber
# Описание: Номер модификации контракта (если контракт изменялся).
# Формат: Строка (String), обычно числовое значение.
# Важность для анализа: Средняя – если модификация ≠ 0, важно для отслеживания изменений в контракте.
"content__award__awardID__awardContractID__transactionNumber": "0"
# Переменная: content__award__awardID__awardContractID__transactionNumber
# Описание: Номер транзакции в рамках контракта (может указывать на уникальные события, связанные с контрактом).
# Формат: Строка (String), обычно числовое значение.
# Важность для анализа: Низкая – редко используется отдельно, но может быть полезна в сложных анализах.
"content__award__awardID__referencedIDVID": "\n            "
# Переменная: content__award__awardID__referencedIDVID
# Описание: Контейнер для информации о связанном IDV (Indefinite Delivery Vehicle) контракте.
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – само поле не несёт информации, но вложенные элементы важны.
"content__award__awardID__referencedIDVID__agencyID": "12C2"
# Переменная: content__award__awardID__referencedIDVID__agencyID
# Описание: Код агентства, выдавшего связанный IDV-контракт.
# Формат: Строка (String).
# Важность для анализа: Средняя – если контракт связан с IDV, полезно для понимания структуры контрактов.
"content__award__awardID__referencedIDVID__agencyID__name": "FOREST SERVICE"
# Переменная: content__award__awardID__referencedIDVID__agencyID__name
# Описание: Название агентства, выдавшего связанный IDV-контракт.
# Формат: Строка (String).
# Важность для анализа: Средняя – удобно для читаемости, но дублирует `referencedIDVID__agencyID`.
"content__award__awardID__referencedIDVID__PIID": "12024B18D9025"
# Переменная: content__award__awardID__referencedIDVID__PIID
# Описание: Уникальный идентификатор (PIID) связанного IDV-контракта.
# Формат: Строка (String).
# Важность для анализа: Высокая – важен для отслеживания структуры контрактов и их связей.
"content__award__awardID__referencedIDVID__modNumber": "0"
# Переменная: content__award__awardID__referencedIDVID__modNumber
# Описание: Номер модификации связанного IDV-контракта.
# Формат: Строка (String), обычно числовое значение.
# Важность для анализа: Средняя – если не "0", означает, что IDV-контракт был модифицирован.
"content__award__relevantContractDates": "\n          "
# Переменная: content__award__relevantContractDates
# Описание: Контейнер, содержащий ключевые даты контракта (дата подписания, вступления в силу, завершения).
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – само поле не несёт информации, но вложенные элементы важны.
"content__award__relevantContractDates__signedDate": "2023-01-01 00:00:00"
# Переменная: content__award__relevantContractDates__signedDate
# Описание: Дата подписания контракта.
# Формат: Дата и время (YYYY-MM-DD HH:MM:SS).
# Важность для анализа: Высокая – фиксирует момент заключения контракта.
"content__award__relevantContractDates__effectiveDate": "2023-01-01 00:00:00"
# Переменная: content__award__relevantContractDates__effectiveDate
# Описание: Дата вступления контракта в силу.
# Формат: Дата и время (YYYY-MM-DD HH:MM:SS).
# Важность для анализа: Высокая – важно для расчёта сроков действия контракта.
"content__award__relevantContractDates__currentCompletionDate": "2023-12-31 00:00:00"
# Переменная: content__award__relevantContractDates__currentCompletionDate
# Описание: Текущая дата завершения контракта (может изменяться в ходе выполнения).
# Формат: Дата и время (YYYY-MM-DD HH:MM:SS).
# Важность для анализа: Средняя – показывает ожидаемую дату окончания контракта.
"content__award__relevantContractDates__ultimateCompletionDate": "2023-12-31 00:00:00"
# Переменная: content__award__relevantContractDates__ultimateCompletionDate
# Описание: Окончательная дата завершения контракта, учитывая все возможные продления.
# Формат: Дата и время (YYYY-MM-DD HH:MM:SS).
# Важность для анализа: Высокая – определяет максимальный срок действия контракта.
"content__award__dollarValues": "\n          "
# Переменная: content__award__dollarValues
# Описание: Контейнер, содержащий финансовые данные по контракту.
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – само поле не несёт информации, но вложенные элементы важны.
"content__award__dollarValues__obligatedAmount": "5000000.00"
# Переменная: content__award__dollarValues__obligatedAmount
# Описание: Сумма, фактически выделенная по контракту (обязательства по оплате).
# Формат: Число с двумя знаками после запятой (Decimal).
# Важность для анализа: Высокая – определяет реальную сумму финансирования.
"content__award__dollarValues__baseAndExercisedOptionsValue": "5000000.00"
# Переменная: content__award__dollarValues__baseAndExercisedOptionsValue
# Описание: Сумма базового контракта плюс все активированные (использованные) опции.
# Формат: Число с двумя знаками после запятой (Decimal).
# Важность для анализа: Средняя – полезно для понимания общей стоимости контракта с учётом использованных опций.
"content__award__dollarValues__baseAndAllOptionsValue": "5000000.00"
# Переменная: content__award__dollarValues__baseAndAllOptionsValue
# Описание: Полная стоимость контракта, включая все возможные опции (даже если они ещё не активированы).
# Формат: Число с двумя знаками после запятой (Decimal).
# Важность для анализа: Высокая – помогает понять максимальный бюджет контракта.
"content__award__totalDollarValues": "\n          "
# Переменная: content__award__totalDollarValues
# Описание: Контейнер, содержащий суммарные финансовые показатели по контракту.
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – само поле не несёт информации, но вложенные элементы важны.
"content__award__totalDollarValues__totalObligatedAmount": "5000000.00"
# Переменная: content__award__totalDollarValues__totalObligatedAmount
# Описание: Общая сумма, выделенная по контракту (включает все модификации и изменения).
# Формат: Число с двумя знаками после запятой (Decimal).
# Важность для анализа: Высокая – ключевой показатель фактического финансирования контракта.
"content__award__totalDollarValues__totalBaseAndExercisedOptionsValue": "5000000.00"
# Переменная: content__award__totalDollarValues__totalBaseAndExercisedOptionsValue
# Описание: Общая стоимость базового контракта и всех использованных (активированных) опций.
# Формат: Число с двумя знаками после запятой (Decimal).
# Важность для анализа: Средняя – помогает оценить, насколько контракт использует доступные опции.
"content__award__totalDollarValues__totalBaseAndAllOptionsValue": "5000000.00"
# Переменная: content__award__totalDollarValues__totalBaseAndAllOptionsValue
# Описание: Полная стоимость контракта, включая базовую сумму и все возможные опции (даже если они не активированы).
# Формат: Число с двумя знаками после запятой (Decimal).
# Важность для анализа: Высокая – позволяет понять максимально возможные затраты по контракту.
"content__award__purchaserInformation": "\n          "
# Переменная: content__award__purchaserInformation
# Описание: Контейнер, содержащий информацию о покупателе (агентстве-заказчике).
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – само поле не несёт информации, но вложенные элементы важны.
"content__award__purchaserInformation__contractingOfficeAgencyID": "12C2"
# Переменная: content__award__purchaserInformation__contractingOfficeAgencyID
# Описание: Код агентства, заключившего контракт.
# Формат: Строка (String).
# Важность для анализа: Высокая – позволяет идентифицировать организацию-заказчика.
"content__award__purchaserInformation__contractingOfficeAgencyID__name": "FOREST SERVICE"
# Переменная: content__award__purchaserInformation__contractingOfficeAgencyID__name
# Описание: Название агентства, заключившего контракт.
# Формат: Строка (String).
# Важность для анализа: Средняя – дублирует `contractingOfficeAgencyID`, но удобна для читаемости.
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
# Переменная: content__award__purchaserInformation__contractingOfficeID
# Описание: Код контрактного офиса, который оформил контракт.
# Формат: Строка (String).
# Важность для анализа: Высокая – позволяет идентифицировать конкретный офис, занимающийся закупками.
"content__award__purchaserInformation__contractingOfficeID__name": "USDA-FS, INCIDENT PROCUREMENT LOGISTICS"
# Переменная: content__award__purchaserInformation__contractingOfficeID__name
# Описание: Название контрактного офиса, заключившего контракт.
# Формат: Строка (String).
# Важность для анализа: Средняя – удобно для читаемости, но может дублировать `contractingOfficeID`.
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
# Переменная: content__award__purchaserInformation__fundingRequestingAgencyID
# Описание: Код агентства, запрашивающего финансирование для контракта.
# Формат: Строка (String).
# Важность для анализа: Высокая – позволяет определить организацию, финансирующую контракт.
"content__award__purchaserInformation__fundingRequestingAgencyID__name": "FOREST SERVICE"
# Переменная: content__award__purchaserInformation__fundingRequestingAgencyID__name
# Описание: Название агентства, запрашивающего финансирование.
# Формат: Строка (String).
# Важность для анализа: Средняя – дублирует `fundingRequestingAgencyID`, но улучшает читаемость.
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
# Переменная: content__award__purchaserInformation__fundingRequestingOfficeID
# Описание: Код офиса, запрашивающего финансирование для контракта.
# Формат: Строка (String).
# Важность для анализа: Высокая – позволяет определить конкретный офис, ответственный за финансирование.
"content__award__purchaserInformation__fundingRequestingOfficeID__name": "USDA FOREST SERVICE"
# Переменная: content__award__purchaserInformation__fundingRequestingOfficeID__name
# Описание: Название офиса, запрашивающего финансирование.
# Формат: Строка (String).
# Важность для анализа: Средняя – дублирует `fundingRequestingOfficeID`, но улучшает читаемость.
"content__award__purchaserInformation__foreignFunding": "X"
# Переменная: content__award__purchaserInformation__foreignFunding
# Описание: Указывает, используется ли иностранное финансирование.
# Формат: Строка (String), обычно "X" означает "NOT APPLICABLE".
# Важность для анализа: Средняя – может быть важна при анализе международного финансирования.
"content__award__purchaserInformation__foreignFunding__description": "NOT APPLICABLE"
# Переменная: content__award__purchaserInformation__foreignFunding__description
# Описание: Описание статуса иностранного финансирования (в данном случае отсутствует).
# Формат: Строка (String).
# Важность для анализа: Низкая – уточняет значение `foreignFunding`, если оно всегда "NOT APPLICABLE", поле можно игнорировать.
"content__award__contractMarketingData": "\n          "
# Переменная: content__award__contractMarketingData
# Описание: Контейнер для маркетинговых данных контракта.
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – само поле не несёт информации, но вложенные элементы могут быть полезны.
"content__award__contractMarketingData__feePaidForUseOfService": "0.00"
# Переменная: content__award__contractMarketingData__feePaidForUseOfService
# Описание: Размер комиссии, уплаченной за использование сервиса (если применимо).
# Формат: Число с двумя знаками после запятой (Decimal).
# Важность для анализа: Низкая – если всегда "0.00", не представляет аналитической ценности.
"content__award__contractData": "\n          "
# Переменная: content__award__contractData
# Описание: Контейнер, содержащий основные данные о контракте.
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – само поле не несёт информации, но вложенные элементы могут быть важны.
"content__award__contractData__contractActionType": "C"
# Переменная: content__award__contractData__contractActionType
# Описание: Код типа действия по контракту.
# Формат: Строка (String).
# Важность для анализа: Средняя – полезно для классификации контрактов, но более важен `contractActionType__description`.
"content__award__contractData__contractActionType__description": "DELIVERY ORDER"
# Переменная: content__award__contractData__contractActionType__description
# Описание: Описание типа действия по контракту (в данном случае – заказ на поставку).
# Формат: Строка (String).
# Важность для анализа: Высокая – ключевая информация о том, каким образом оформлен контракт.
"content__award__contractData__typeOfContractPricing": "J"
# Переменная: content__award__contractData__typeOfContractPricing
# Описание: Код типа ценообразования по контракту.
# Формат: Строка (String).
# Важность для анализа: Средняя – полезно при обработке данных, но более важно описание.
"content__award__contractData__typeOfContractPricing__description": "FIRM FIXED PRICE"
# Переменная: content__award__contractData__typeOfContractPricing__description
# Описание: Тип ценообразования – фиксированная цена (FIRM FIXED PRICE).
# Формат: Строка (String).
# Важность для анализа: Высокая – определяет, как формируется стоимость контракта.
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
Примеры значений:
- `"HURRICANE RECOVERY"` – контракт связан с восстановлением после урагана.
- `"COVID-19"` – контракт выделен в рамках борьбы с пандемией.
- `"NATIONAL DEFENSE"` – контракт относится к вопросам национальной обороны.
- `"NONE"` – контракт не связан с особыми национальными интересами.
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
# Описание: Текстовое описание значения `costOrPricingData`.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует `costOrPricingData`, полезно только для удобства чтения.
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
# Переменная: content__award__contractData__descriptionOfContractRequirement
# Описание: Описание требований к контракту – цель и предмет закупки.
# Формат: Строка (String).
# Важность для анализа: Высокая – ключевое поле, объясняющее суть контракта.
"content__award__contractData__inherentlyGovernmentalFunction": "OT        "
# Переменная: content__award__contractData__inherentlyGovernmentalFunction
# Описание: Код, указывающий, выполняет ли контракт функции, которые должны оставаться в руках правительства.
# Формат: Строка (String), возможные значения:
  - `"IG"` – Inherently Governmental (Функции, выполняемые исключительно государственными служащими).
  - `"OT"` – Other Functions (Другие функции, которые могут выполняться подрядчиками).
  - `"CM"` – Closely Associated with Inherently Governmental Functions (Функции, тесно связанные с правительственными, но переданные подрядчику).
# Важность для анализа: Средняя – если значение `"IG"`, контракт может требовать повышенного контроля.
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
# Описание: Текстовое описание значения `GFE-GFP`, указывающее, используется ли государственное имущество.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует `GFE-GFP`, полезно для удобства чтения.
"content__award__contractData__undefinitizedAction": "X"
# Переменная: content__award__contractData__undefinitizedAction
# Описание: Указывает, является ли действие по контракту "неопределённым" (Undefinitized Contract Action, UCA) – когда работа начинается до окончательного соглашения о стоимости.
# Формат: Строка (String), обычно "Y" (Yes) или "X" (No).
# Важность для анализа: Средняя – если "Y", означает, что контракт может содержать неопределённые условия.
"content__award__contractData__undefinitizedAction__description": "NO"
# Переменная: content__award__contractData__undefinitizedAction__description
# Описание: Описание, содержит ли контракт неопределённые условия.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует `undefinitizedAction`, полезно для удобочитаемости.
"content__award__contractData__consolidatedContract": "D"
# Переменная: content__award__contractData__consolidatedContract
# Описание: Указывает, является ли контракт консолидированным (объединяет несколько контрактов или требований в один).
# Формат: Строка (String), возможные значения:
  - "Y" – Да, контракт консолидирован.
  - "N" – Нет, контракт не является консолидированным.
  - "D" – Освобождён от требований по консолидации.
# Важность для анализа: Средняя – важно при анализе крупных контрактов, объединяющих несколько потребностей.
"content__award__contractData__consolidatedContract__description": "NOT CONSOLIDATED"
# Переменная: content__award__contractData__consolidatedContract__description
# Описание: Указывает, является ли контракт консолидированным (объединяющим несколько контрактов в один).
# Формат: Строка (String).
## Возможные значения:
  - `"CONSOLIDATED"` – Контракт объединяет несколько требований в один.
  - `"NOT CONSOLIDATED"` – Контракт не является консолидированным.
  - `"EXEMPT"` – Контракт освобождён от требований консолидации.
# Важность для анализа: Средняя – влияет на анализ закупок, особенно крупных контрактов.
"content__award__contractData__performanceBasedServiceContract": "N"
# Переменная: content__award__contractData__performanceBasedServiceContract
# Описание: Указывает, является ли контракт сервисным контрактом, основанным на показателях эффективности (Performance-Based Acquisition, PBA).
# Формат: Строка (String).
## Возможные значения:
  - `"Y"` – Контракт основан на показателях эффективности.
  - `"N"` – Контракт не является PBA.
# Важность для анализа: Средняя – важно для анализа качества услуг, поставляемых по контракту.
"content__award__contractData__performanceBasedServiceContract__description": "NO - SERVICE WHERE PBA IS NOT USED."
# Переменная: content__award__contractData__performanceBasedServiceContract__description
# Описание: Текстовое описание значения `performanceBasedServiceContract`, уточняющее, применяется ли Performance-Based Acquisition.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует `performanceBasedServiceContract`, полезно для удобочитаемости.
"content__award__contractData__multiYearContract": "N"
# Переменная: content__award__contractData__multiYearContract
# Описание: Указывает, является ли контракт многолетним.
# Формат: Строка (String).
## Возможные значения:
  - `"Y"` – Контракт рассчитан на несколько лет.
  - `"N"` – Контракт не является многолетним.
# Важность для анализа: Высокая – многолетние контракты важны для долгосрочного бюджетного планирования.
"content__award__contractData__multiYearContract__description": "NO"
# Переменная: content__award__contractData__multiYearContract__description
# Описание: Текстовое описание значения `multiYearContract`, уточняющее, является ли контракт многолетним.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует `multiYearContract`, полезно для удобочитаемости.
"content__award__contractData__contingencyHumanitarianPeacekeepingOperation": "X"
# Переменная: content__award__contractData__contingencyHumanitarianPeacekeepingOperation
# Описание: Указывает, связан ли контракт с операциями по чрезвычайным ситуациям, гуманитарной помощи или миротворчеству.
# Формат: Строка (String).
## Возможные значения:
  - `"Y"` – Да, контракт связан с миротворческими, гуманитарными или чрезвычайными операциями.
  - `"N"` – Нет, контракт не связан с такими операциями.
  - `"X"` – Не применимо.
# Важность для анализа: Средняя – может быть важно при анализе контрактов в рамках государственных и военных программ.
"content__award__contractData__contingencyHumanitarianPeacekeepingOperation__description": "NOT APPLICABLE"
# Переменная: content__award__contractData__contingencyHumanitarianPeacekeepingOperation__description
# Описание: Описание значения `contingencyHumanitarianPeacekeepingOperation`, указывающее, связан ли контракт с гуманитарными операциями.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.
"content__award__contractData__referencedIDVMultipleOrSingle": "S"
# Переменная: content__award__contractData__referencedIDVMultipleOrSingle
# Описание: Указывает, является ли связанный IDV (Indefinite Delivery Vehicle) контрактом с одним или несколькими поставщиками.
# Формат: Строка (String).
## Возможные значения:
  - `"S"` – **Single Award** – Контракт присуждён только одному поставщику.
  - `"M"` – **Multiple Award** – Контракт может включать нескольких поставщиков.
# Важность для анализа: Высокая – важно для понимания структуры контрактов и конкуренции.
"content__award__contractData__referencedIDVMultipleOrSingle__description": "SINGLE AWARD"
# Переменная: content__award__contractData__referencedIDVMultipleOrSingle__description
# Описание: Описание значения `referencedIDVMultipleOrSingle`, уточняющее тип присуждения контракта.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.
"content__award__contractData__referencedIDVType": "B"
# Переменная: content__award__contractData__referencedIDVType
# Описание: Указывает тип IDV-контракта (Indefinite Delivery Vehicle).
# Формат: Строка (String).
## Возможные значения:
  - `"A"` – BOA (Basic Ordering Agreement) – Основное соглашение о заказе.
  - `"B"` – IDC (Indefinite Delivery Contract) – Контракт на неопределённую поставку.
  - `"C"` – FSS (Federal Supply Schedule) – Контракт по федеральному графику поставок.
  - `"D"` – GWAC (Government-Wide Acquisition Contract) – Контракт для госзакупок в масштабах всего правительства.
# Важность для анализа: Высокая – важно при анализе типов контрактов и их условий.
"content__award__contractData__referencedIDVType__description": "IDC"
# Переменная: content__award__contractData__referencedIDVType__description
# Описание: Описание значения `referencedIDVType`, уточняющее тип IDV-контракта.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.
"content__award__contractData__contractFinancing": "Z"
# Переменная: content__award__contractData__contractFinancing
# Описание: Указывает, используется ли в контракте механизм финансирования.
# Формат: Строка (String).
## Возможные значения:
  - `"A"` – **Advance Payment** – Предоплата.
  - `"B"` – **Progress Payment Based on Cost** – Прогрессивные платежи на основе затрат.
  - `"C"` – **Progress Payment Based on Milestones** – Прогрессивные платежи на основе выполнения этапов.
  - `"D"` – **Loan Guarantee** – Гарантированное государственное финансирование (заём).
  - `"E"` – **Private Financing** – Частное финансирование.
  - `"Z"` – **Not Applicable** – Контракт не предусматривает финансирование.
# Важность для анализа: Средняя – важно, если контракт связан с предоплатой или частным финансированием.
"content__award__contractData__contractFinancing__description": "NOT APPLICABLE"
# Переменная: content__award__contractData__contractFinancing__description
# Описание: Описание значения `contractFinancing`, указывающее, используется ли механизм финансирования в контракте.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле `contractFinancing`, полезно для удобочитаемости.

"content__award__contractData__purchaseCardAsPaymentMethod": "N"
# Переменная: content__award__contractData__purchaseCardAsPaymentMethod
# Описание: Указывает, используется ли в качестве метода оплаты правительственная покупательная карта (Government Purchase Card).
# Формат: Строка (String).
## Возможные значения:
  - `"Y"` – Да, оплата производится с помощью Government Purchase Card.
  - `"N"` – Нет, другой метод оплаты.
# Важность для анализа: Средняя – важно для определения механизмов расчёта по контракту.

"content__award__contractData__purchaseCardAsPaymentMethod__description": "NO"
# Переменная: content__award__contractData__purchaseCardAsPaymentMethod__description
# Описание: Описание значения `purchaseCardAsPaymentMethod`, уточняющее, используется ли покупательная карта.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__contractData__numberOfActions": "1"
# Переменная: content__award__contractData__numberOfActions
# Описание: Количество действий (транзакций) по данному контракту.
# Формат: Целое число (Integer).
# Важность для анализа: Средняя – полезно для отслеживания количества операций по контракту.

"content__award__legislativeMandates": "\n          "
# Переменная: content__award__legislativeMandates
# Описание: Контейнер для законодательных требований, применимых к контракту.
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – само поле не содержит информации, но вложенные элементы могут быть важны.

"content__award__legislativeMandates__ClingerCohenAct": "N"
# Переменная: content__award__legislativeMandates__ClingerCohenAct
# Описание: Указывает, применяется ли к контракту Закон Клинжера-Коэна (Clinger-Cohen Act), регулирующий IT-закупки в федеральных агентствах.
# Формат: Строка (String).
## Возможные значения:
  - `"Y"` – Да, контракт подпадает под регулирование Clinger-Cohen Act.
  - `"N"` – Нет, контракт не подпадает под это законодательство.
# Важность для анализа: Средняя – важно, если контракт связан с IT-закупками.

"content__award__legislativeMandates__ClingerCohenAct__description": "NO"
# Переменная: content__award__legislativeMandates__ClingerCohenAct__description
# Описание: Описание значения `ClingerCohenAct`, уточняющее, применяется ли это законодательство.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__legislativeMandates__materialsSuppliesArticlesEquipment": "N"
# Переменная: content__award__legislativeMandates__materialsSuppliesArticlesEquipment
# Описание: Указывает, регулируется ли контракт законодательством, касающимся поставки материалов, оборудования и товаров.
# Формат: Строка (String).
## Возможные значения:
  - `"Y"` – Да, контракт подпадает под регулирование по поставкам материалов и оборудования.
  - `"N"` – Нет, контракт не регулируется специальными требованиями к поставкам.
# Важность для анализа: Средняя – важно при анализе контрактов, связанных с поставками оборудования.
"content__award__legislativeMandates__materialsSuppliesArticlesEquipment__description": "NO"
# Переменная: content__award__legislativeMandates__materialsSuppliesArticlesEquipment__description
# Описание: Описание значения `materialsSuppliesArticlesEquipment`, указывающее, регулируется ли контракт поставками материалов и оборудования.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__legislativeMandates__laborStandards": "Y"
# Переменная: content__award__legislativeMandates__laborStandards
# Описание: Указывает, применяются ли к контракту требования по стандартам труда.
# Формат: Строка (String).
## Возможные значения:
  - `"Y"` – Да, контракт должен соответствовать требованиям трудового законодательства.
  - `"N"` – Нет, контракт не подпадает под регулирование трудовых стандартов.
# Важность для анализа: Высокая – важно при анализе контрактов, связанных с наёмным трудом и минимальными стандартами оплаты.

"content__award__legislativeMandates__laborStandards__description": "YES"
# Переменная: content__award__legislativeMandates__laborStandards__description
# Описание: Описание значения `laborStandards`, уточняющее, применяются ли стандарты труда.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__legislativeMandates__constructionWageRateRequirements": "N"
# Переменная: content__award__legislativeMandates__constructionWageRateRequirements
# Описание: Указывает, регулируется ли контракт требованиями к оплате труда в строительной отрасли (Davis-Bacon Act).
# Формат: Строка (String).
## Возможные значения:
  - `"Y"` – Да, контракт должен соответствовать требованиям по строительным ставкам оплаты.
  - `"N"` – Нет, требования по ставкам оплаты в строительной отрасли не применяются.
# Важность для анализа: Средняя – важно для строительных контрактов и оценки условий оплаты труда.

"content__award__legislativeMandates__constructionWageRateRequirements__description": "NO"
# Переменная: content__award__legislativeMandates__constructionWageRateRequirements__description
# Описание: Описание значения `constructionWageRateRequirements`, уточняющее, регулируется ли контракт требованиями по ставкам оплаты в строительстве.
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
## Возможные значения:
  - `"S"` – Контракт подпадает под **Service Contract Inventory (FAR 4.17)** – инвентаризацию сервисных контрактов.
  - `"C"` – Контракт подпадает под **Construction Compliance** – дополнительные строительные требования.
  - `"E"` – Контракт подпадает под **Energy Efficiency Reporting** – отчетность по энергоэффективности.
  - `"N"` – Не требует дополнительной отчетности.
# Важность для анализа: Средняя – важно для определения дополнительных обязательств подрядчика.

"content__award__legislativeMandates__listOfAdditionalReportingValues__additionalReportingValue__description": "SERVICE CONTRACT INVENTORY (FAR 4.17)"
# Переменная: content__award__legislativeMandates__listOfAdditionalReportingValues__additionalReportingValue__description
# Описание: Описание кода `additionalReportingValue`, уточняющее, какое требование по отчетности применяется.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.
"content__award__legislativeMandates__interagencyContractingAuthority": "X"
# Переменная: content__award__legislativeMandates__interagencyContractingAuthority
# Описание: Указывает, регулируется ли контракт межведомственным соглашением (Interagency Contracting Authority).
# Формат: Строка (String).
## Возможные значения:
  - `"Y"` – Да, контракт подпадает под межведомственное соглашение.
  - `"N"` – Нет, контракт не связан с межведомственными закупками.
  - `"X"` – Не применимо.
# Важность для анализа: Средняя – важно, если контракт заключён в рамках совместных закупок между агентствами.

"content__award__legislativeMandates__interagencyContractingAuthority__description": "NOT APPLICABLE"
# Переменная: content__award__legislativeMandates__interagencyContractingAuthority__description
# Описание: Описание значения `interagencyContractingAuthority`, уточняющее, подпадает ли контракт под межведомственное соглашение.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__productOrServiceInformation": "\n          "
# Переменная: content__award__productOrServiceInformation
# Описание: Контейнер, содержащий информацию о продукции или услуге, связанной с контрактом.
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – само поле не несёт информации, но вложенные элементы важны.

"content__award__productOrServiceInformation__productOrServiceCode": "F003"
# Переменная: content__award__productOrServiceInformation__productOrServiceCode
# Описание: Код, обозначающий тип продукции или услуги, предоставляемой по контракту.
# Формат: Строка (String).
## Примеры значений:
  - `"F003"` – Поддержка природных ресурсов / лесные пожары (fire suppression).
  - `"R706"` – Логистическая поддержка.
  - `"D399"` – IT-услуги.
  - `"J099"` – Техническое обслуживание оборудования.
# Важность для анализа: Высокая – важно для классификации контрактов.

"content__award__productOrServiceInformation__productOrServiceCode__description": "NATURAL RESOURCES/CONSERVATION- FOREST-RANGE FIRE SUPPRESSION/PRESUPPRESSION"
# Переменная: content__award__productOrServiceInformation__productOrServiceCode__description
# Описание: Описание кода `productOrServiceCode`, уточняющее, какие услуги или товары включает контракт.
# Формат: Строка (String).
# Важность для анализа: Средняя – полезно для интерпретации `productOrServiceCode`, но можно заменить справочником кодов.

"content__award__productOrServiceInformation__productOrServiceCode__productOrServiceType": "SERVICE"
# Переменная: content__award__productOrServiceInformation__productOrServiceCode__productOrServiceType
# Описание: Определяет, относится ли контракт к категории "товары" (Product) или "услуги" (Service).
# Формат: Строка (String).
## Возможные значения:
  - `"PRODUCT"` – Контракт связан с поставкой товаров.
  - `"SERVICE"` – Контракт связан с предоставлением услуг.
# Важность для анализа: Высокая – помогает классифицировать контракты по типу.
"content__award__productOrServiceInformation__contractBundling": "H"
# Переменная: content__award__productOrServiceInformation__contractBundling
# Описание: Указывает, является ли контракт "bundled" (объединённым из нескольких меньших контрактов).
# Формат: Строка (String).
## Возможные значения:
  - `"A"` – Полностью объединённый контракт.
  - `"B"` – Частично объединённый контракт.
  - `"C"` – Освобождён от требований по объединению.
  - `"H"` – Не объединённый (Not Bundled).
# Важность для анализа: Средняя – важно при анализе влияния на малый бизнес и конкуренцию.

"content__award__productOrServiceInformation__contractBundling__description": "NOT BUNDLED"
# Переменная: content__award__productOrServiceInformation__contractBundling__description
# Описание: Описание значения `contractBundling`, указывающее, является ли контракт объединённым.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__productOrServiceInformation__principalNAICSCode": "115310"
# Переменная: content__award__productOrServiceInformation__principalNAICSCode
# Описание: Основной код отрасли по системе NAICS (North American Industry Classification System).
# Формат: Строка (String).
## Примеры значений:
  - `"115310"` – Лесное хозяйство и борьба с пожарами.
  - `"541512"` – IT-консалтинг и разработка ПО.
  - `"236220"` – Коммерческое строительство.
# Важность для анализа: Высокая – позволяет анализировать контракты по отраслям.

"content__award__productOrServiceInformation__principalNAICSCode__description": "SUPPORT ACTIVITIES FOR FORESTRY"
# Переменная: content__award__productOrServiceInformation__principalNAICSCode__description
# Описание: Описание кода NAICS, указывающее, к какой отрасли относится контракт.
# Формат: Строка (String).
# Важность для анализа: Средняя – дублирует код NAICS, но делает его понятнее.

"content__award__productOrServiceInformation__recoveredMaterialClauses": "E"
# Переменная: content__award__productOrServiceInformation__recoveredMaterialClauses
# Описание: Указывает, есть ли требования по использованию переработанных материалов.
# Формат: Строка (String).
## Возможные значения:
  - `"A"` – Требования по переработанным материалам включены.
  - `"C"` – Требования отсутствуют, устойчивость не учитывается.
  - `"E"` – Контракт связан с био-материалами (Bio-Based).
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
## Возможные значения:
  - `"A"` – Компания, принадлежащая гражданам США.
  - `"B"` – Компания, зарегистрированная в США, но с иностранным капиталом.
  - `"C"` – Иностранная компания.
# Важность для анализа: Средняя – важно при анализе контрактов с иностранными поставщиками.
"content__award__productOrServiceInformation__manufacturingOrganizationType__description": "FOREIGN-OWNED BUSINESS INCORPORATED IN THE U.S."
# Переменная: content__award__productOrServiceInformation__manufacturingOrganizationType__description
# Описание: Описание типа организации-производителя, уточняющее, является ли компания иностранной или национальной.
# Формат: Строка (String).
## Возможные значения:
  - `"U.S.-OWNED BUSINESS"` – Компания, принадлежащая гражданам США.
  - `"FOREIGN-OWNED BUSINESS INCORPORATED IN THE U.S."` – Иностранная компания, зарегистрированная в США.
  - `"FOREIGN BUSINESS"` – Иностранная компания без регистрации в США.
# Важность для анализа: Средняя – полезно при анализе участия иностранных компаний в госзакупках.

"content__award__productOrServiceInformation__useOfEPADesignatedProducts": "E"
# Переменная: content__award__productOrServiceInformation__useOfEPADesignatedProducts
# Описание: Указывает, требует ли контракт использование продуктов, сертифицированных Агентством по охране окружающей среды (EPA).
# Формат: Строка (String).
## Возможные значения:
  - `"A"` – Использование продуктов, утверждённых EPA, **обязательно**.
  - `"C"` – Использование продуктов, утверждённых EPA, **не требуется**.
  - `"E"` – Использование EPA-продуктов **не определено** или **не применимо**.
# Важность для анализа: Средняя – важно при анализе контрактов, связанных с экологическими стандартами.

"content__award__productOrServiceInformation__useOfEPADesignatedProducts__description": "NOT REQUIRED"
# Переменная: content__award__productOrServiceInformation__useOfEPADesignatedProducts__description
# Описание: Описание значения `useOfEPADesignatedProducts`, уточняющее, требуется ли использование утверждённых EPA продуктов.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.

"content__award__productOrServiceInformation__countryOfOrigin": "USA"
# Переменная: content__award__productOrServiceInformation__countryOfOrigin
# Описание: Код страны происхождения товара или услуги.
# Формат: Строка (String).
## Примеры значений:
  - `"USA"` – Соединённые Штаты Америки.
  - `"CHN"` – Китай.
  - `"DEU"` – Германия.
# Важность для анализа: Высокая – важно при анализе импорта и национального производства.

"content__award__productOrServiceInformation__countryOfOrigin__name": "UNITED STATES"
# Переменная: content__award__productOrServiceInformation__countryOfOrigin__name
# Описание: Название страны происхождения товара или услуги.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует код страны, полезно для удобочитаемости.

"content__award__productOrServiceInformation__placeOfManufacture": "C"
# Переменная: content__award__productOrServiceInformation__placeOfManufacture
# Описание: Указывает, является ли контрактным предметом готовый производственный продукт.
# Формат: Строка (String).
## Возможные значения:
  - `"A"` – Изготовлено в США.
  - `"B"` – Изготовлено за границей.
  - `"C"` – Не является конечным производственным продуктом (например, услуга или сборка из нескольких компонентов).
# Важность для анализа: Средняя – полезно при анализе контрактов на производство.

"content__award__productOrServiceInformation__placeOfManufacture__description": "NOT A MANUFACTURED END PRODUCT"
# Переменная: content__award__productOrServiceInformation__placeOfManufacture__description
# Описание: Описание значения `placeOfManufacture`, уточняющее, является ли товар конечным продуктом производства.
# Формат: Строка (String).
# Важность для анализа: Низкая – дублирует основное поле, полезно для удобочитаемости.
"content__award__vendor": "\n          "
# Переменная: content__award__vendor
# Описание: Контейнер, содержащий информацию о поставщике (подрядчике).
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – само поле не несёт информации, но вложенные элементы важны.

"content__award__vendor__vendorHeader": "\n            "
# Переменная: content__award__vendor__vendorHeader
# Описание: Контейнер, содержащий основные сведения о поставщике.
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – само поле не содержит информации, но вложенные элементы важны.

"content__award__vendor__vendorHeader__vendorName": "PERIMETER SOLUTIONS LP"
# Переменная: content__award__vendor__vendorHeader__vendorName
# Описание: Официальное название поставщика, заключившего контракт.
# Формат: Строка (String).
# Важность для анализа: Высокая – ключевая информация о подрядчике.

"content__award__vendor__vendorSiteDetails": "\n            "
# Переменная: content__award__vendor__vendorSiteDetails
# Описание: Контейнер, содержащий детальную информацию о местонахождении поставщика.
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – само поле не содержит информации, но вложенные элементы могут быть полезны.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators": "\n              "
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators
# Описание: Контейнер, содержащий социально-экономические характеристики поставщика (например, статус малого бизнеса, владение ветеранами).
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – само поле не содержит информации, но вложенные элементы могут быть полезны.
"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isAlaskanNativeOwnedCorporationOrFirm": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isAlaskanNativeOwnedCorporationOrFirm
# Описание: Указывает, является ли компания корпорацией или фирмой, принадлежащей коренным жителям Аляски.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для контрактов, выделяемых для поддержки коренных народов.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isAmericanIndianOwned": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isAmericanIndianOwned
# Описание: Указывает, принадлежит ли компания представителю коренного населения Америки.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для контрактов, выделяемых для поддержки коренных американцев.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isIndianTribe": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isIndianTribe
# Описание: Указывает, является ли компания предприятием, принадлежащим индейскому племени.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – может быть важным для контрактов, предоставляемых племенным организациям.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isNativeHawaiianOwnedOrganizationOrFirm": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isNativeHawaiianOwnedOrganizationOrFirm
# Описание: Указывает, принадлежит ли компания представителям коренного населения Гавайев.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно при анализе контрактов, поддерживающих бизнес коренных гавайцев.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isTriballyOwnedFirm": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isTriballyOwnedFirm
# Описание: Указывает, принадлежит ли компания племенной организации.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – используется при выделении контрактов для племенных организаций.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isSmallBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isSmallBusiness
# Описание: Указывает, относится ли компания к категории малого бизнеса.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Высокая – важно для контрактов, выделяемых в рамках программ поддержки малого бизнеса.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isVeteranOwned": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isVeteranOwned
# Описание: Указывает, принадлежит ли компания ветерану вооружённых сил США.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно при анализе контрактов, выделяемых для ветеранов.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isServiceRelatedDisabledVeteranOwnedBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isServiceRelatedDisabledVeteranOwnedBusiness
# Описание: Указывает, принадлежит ли компания ветерану с ограниченными возможностями, связанными со службой.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Высокая – имеет значение для контрактов, выделяемых в поддержку ветеранов-инвалидов.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isWomenOwned": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isWomenOwned
# Описание: Указывает, принадлежит ли компания женщине.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Высокая – важно при анализе контрактов, выделяемых в поддержку женского бизнеса.
"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned": "\n                "
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned
# Описание: Контейнер, указывающий, является ли компания бизнесом, принадлежащим представителям меньшинств.
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – не несёт прямой информации, но вложенные элементы могут быть важными.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isMinorityOwned": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isMinorityOwned
# Описание: Указывает, является ли компания бизнесом, принадлежащим представителю меньшинства.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для анализа контракта в контексте поддержки меньшинств.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isSubContinentAsianAmericanOwnedBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isSubContinentAsianAmericanOwnedBusiness
# Описание: Указывает, принадлежит ли компания бизнесу, управляемому американцами из Южной Азии.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для поддержания равенства возможностей для бизнеса.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isAsianPacificAmericanOwnedBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isAsianPacificAmericanOwnedBusiness
# Описание: Указывает, принадлежит ли компания бизнесу, управляемому американцами азиатского и тихоокеанского происхождения.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – поддержка азиатских и тихоокеанских американцев.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isBlackAmericanOwnedBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isBlackAmericanOwnedBusiness
# Описание: Указывает, принадлежит ли компания бизнесу, управляемому чернокожими американцами.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для анализа контрактов, поддерживающих чернокожий бизнес.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isHispanicAmericanOwnedBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isHispanicAmericanOwnedBusiness
# Описание: Указывает, принадлежит ли компания бизнесу, управляемому американцами латинского происхождения.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для анализа контрактов, поддерживающих латинский бизнес.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isNativeAmericanOwnedBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isNativeAmericanOwnedBusiness
# Описание: Указывает, принадлежит ли компания бизнесу, управляемому коренными американцами.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для анализа контрактов, поддерживающих коренные американцы.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isOtherMinorityOwned": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__minorityOwned__isOtherMinorityOwned
# Описание: Указывает, принадлежит ли компания другому бизнесу, управляемому представителем меньшинства.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для включения других групп меньшинств.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isVerySmallBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isVerySmallBusiness
# Описание: Указывает, является ли компания очень малым бизнесом.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Высокая – важно для анализа контрактов, направленных на поддержку очень малого бизнеса.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isWomenOwnedSmallBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isWomenOwnedSmallBusiness
# Описание: Указывает, принадлежит ли компания малому бизнесу, управляемому женщиной.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Высокая – важный индикатор для контрактов, поддерживающих женский малый бизнес.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isEconomicallyDisadvantagedWomenOwnedSmallBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isEconomicallyDisadvantagedWomenOwnedSmallBusiness
# Описание: Указывает, принадлежит ли компания экономически обездоленной женщине, владеющей малым бизнесом.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Высокая – важное поле для анализа поддержки экономически обездоленных женщин.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isJointVentureWomenOwnedSmallBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isJointVentureWomenOwnedSmallBusiness
# Описание: Указывает, является ли компания совместным предприятием, управляемым женщинами.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для понимания структуры совместных предприятий с участием женщин.

"content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isJointVentureEconomicallyDisadvantagedWomenOwnedSmallBusiness": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isJointVentureEconomicallyDisadvantagedWomenOwnedSmallBusiness
# Описание: Указывает, является ли компания совместным предприятием, управляемым экономически обездоленными женщинами.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для анализа поддержки совместных предприятий, принадлежащих экономически обездоленным женщинам.
"content__award__vendor__vendorSiteDetails__vendorBusinessTypes": "\n              "
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes
# Описание: Контейнер, содержащий информацию о типах бизнеса поставщика.
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – не несёт данных само по себе, но вложенные элементы важны.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__isCommunityDevelopedCorporationOwnedFirm": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__isCommunityDevelopedCorporationOwnedFirm
# Описание: Указывает, является ли компания корпорацией, принадлежащей развивающемуся сообществу.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для анализа контрактов, поддерживающих развивающиеся сообщества.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__isLaborSurplusAreaFirm": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__isLaborSurplusAreaFirm
# Описание: Указывает, является ли компания фирмой, расположенной в районе с избытком рабочей силы.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для контрактов, направленных на поддержку районов с высоким уровнем безработицы.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__federalGovernment": "\n                "
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__federalGovernment
# Описание: Контейнер для информации о том, является ли поставщик федеральным правительственным учреждением.
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – само поле не содержит данных, но вложенные элементы полезны.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__federalGovernment__isFederalGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__federalGovernment__isFederalGovernment
# Описание: Указывает, является ли поставщик федеральным правительственным агентством.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для различения государственных и частных поставщиков.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__federalGovernment__isFederallyFundedResearchAndDevelopmentCorp": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__federalGovernment__isFederallyFundedResearchAndDevelopmentCorp
# Описание: Указывает, является ли поставщик корпорацией, финансируемой федеральным правительством для исследований и разработок.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для контрактов, связанных с государственными исследовательскими корпорациями.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__federalGovernment__isFederalGovernmentAgency": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__federalGovernment__isFederalGovernmentAgency
# Описание: Указывает, является ли поставщик федеральным государственным агентством.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – помогает различать частные компании и государственные учреждения.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__isStateGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__isStateGovernment
# Описание: Указывает, является ли поставщик государственным учреждением на уровне штата.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для контрактов, которые могут быть выделены государственным учреждениям штатов.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment": "\n"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment
# Описание: Контейнер для информации о том, является ли поставщик местным государственным учреждением.
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – само поле не несёт данных, но вложенные элементы полезны.              ",
"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isLocalGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isLocalGovernment
# Описание: Указывает, является ли поставщик местным государственным учреждением (например, городом или округом).
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для различения местных государственных организаций от частных компаний.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isCityLocalGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isCityLocalGovernment
# Описание: Указывает, является ли поставщик местным государственным учреждением на уровне города.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – помогает идентифицировать компании, работающие с городскими властями.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isCountyLocalGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isCountyLocalGovernment
# Описание: Указывает, является ли поставщик местным государственным учреждением на уровне округа.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – полезно для анализа контрактов с округами.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isInterMunicipalLocalGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isInterMunicipalLocalGovernment
# Описание: Указывает, является ли поставщик межмуниципальным местным правительственным учреждением.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – может быть полезно для контрактов, направленных на межмуниципальное сотрудничество.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isLocalGovernmentOwned": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isLocalGovernmentOwned
# Описание: Указывает, является ли поставщик учреждением, принадлежащим местному правительству.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для определения собственности на местном уровне.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isMunicipalityLocalGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isMunicipalityLocalGovernment
# Описание: Указывает, является ли поставщик муниципальным местным государственным учреждением.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для определения роли компании в муниципальном управлении.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isSchoolDistrictLocalGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isSchoolDistrictLocalGovernment
# Описание: Указывает, является ли поставщик частью местного школьного округа.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для контрактов, связанных с образованием на местном уровне.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isTownshipLocalGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__localGovernment__isTownshipLocalGovernment
# Описание: Указывает, является ли поставщик частью местного правительства на уровне поселений (township).
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – полезно для различения поставщиков, работающих на уровне малых населённых пунктов.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__isTribalGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__isTribalGovernment
# Описание: Указывает, является ли поставщик частью племенного правительства.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для поддержки контрактов с племенными организациями.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__isForeignGovernment": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__isForeignGovernment
# Описание: Указывает, является ли поставщик иностранным государственным учреждением.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – полезно для определения поставщиков, связанных с правительствами других стран.
"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType": "\n                "
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType
# Описание: Контейнер, содержащий информацию о типе бизнеса или организации поставщика.
# Формат: Строка (String), обычно XML-структура или пустая строка.
# Важность для анализа: Низкая – само поле не несёт данных, но вложенные элементы полезны.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isCorporateEntityNotTaxExempt": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isCorporateEntityNotTaxExempt
# Описание: Указывает, является ли организация корпоративным предприятием, не освобождённым от налогов.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – полезно для различения налоговых категорий организаций.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isCorporateEntityTaxExempt": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isCorporateEntityTaxExempt
# Описание: Указывает, является ли организация корпоративным предприятием, освобождённым от налогов.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – важно для анализа налогового статуса организации.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isPartnershipOrLimitedLiabilityPartnership": "true"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isPartnershipOrLimitedLiabilityPartnership
# Описание: Указывает, является ли организация партнёрством или партнёрством с ограниченной ответственностью.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Высокая – важно для определения типа организации и юридической структуры бизнеса.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isSolePropreitorship": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isSolePropreitorship
# Описание: Указывает, является ли организация индивидуальным предпринимателем.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – полезно для определения типа юридической структуры бизнеса.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isSmallAgriculturalCooperative": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isSmallAgriculturalCooperative
# Описание: Указывает, является ли организация малой сельскохозяйственной кооперативной организацией.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Низкая – полезно для специфичных типов контрактов, связанных с сельским хозяйством.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isInternationalOrganization": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isInternationalOrganization
# Описание: Указывает, является ли организация международной.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – полезно для определения участия международных организаций в контрактах.

"content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isUSGovernmentEntity": "false"
# Переменная: content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isUSGovernmentEntity
# Описание: Указывает, является ли организация федеральным правительственным учреждением США.
# Формат: Булево (Boolean), `"true"` или `"false"`.
# Важность для анализа: Средняя – полезно для анализа контрактов с федеральными правительственными учреждениями США.
    "content__award__vendor__vendorSiteDetails__vendorLineOfBusiness": "\n              ",
    "content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isCommunityDevelopmentCorporation": "false",
    "content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isDomesticShelter": "false",
    "content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isEducationalInstitution": "false",
    "content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isFoundation": "false",
    "content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isHospital": "false",
    "content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isManufacturerOfGoods": "false",
    "content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isVeterinaryHospital": "false",
    "content__award__vendor__vendorSiteDetails__vendorLineOfBusiness__isHispanicServicingInstitution": "false",
    "content__award__vendor__vendorSiteDetails__vendorRelationshipWithFederalGovernment": "\n              ",
    "content__award__vendor__vendorSiteDetails__vendorRelationshipWithFederalGovernment__receivesContracts": "false",
    "content__award__vendor__vendorSiteDetails__vendorRelationshipWithFederalGovernment__receivesGrants": "false",
    "content__award__vendor__vendorSiteDetails__vendorRelationshipWithFederalGovernment__receivesContractsAndGrants": "true",
    "content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity": "\n              ",
    "content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isAirportAuthority": "false",
    "content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isCouncilOfGovernments": "false",
    "content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isHousingAuthoritiesPublicOrTribal": "false",
    "content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isInterstateEntity": "false",
    "content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isPlanningCommission": "false",
    "content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isPortAuthority": "false",
    "content__award__vendor__vendorSiteDetails__typeOfGovernmentEntity__isTransitAuthority": "false",
    "content__award__vendor__vendorSiteDetails__vendorOrganizationFactors": "\n              ",
    "content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__isSubchapterSCorporation": "false",
    "content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__isLimitedLiabilityCorporation": "false",
    "content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__isForeignOwnedAndLocated": "true",
    "content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__profitStructure": "\n                ",
    "content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__profitStructure__isForProfitOrganization": "true",
    "content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__profitStructure__isNonprofitOrganization": "false",
    "content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__profitStructure__isOtherNotForProfitOrganization": "false",
    "content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__isShelteredWorkshop": "false",
    "content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__stateOfIncorporation": "DE",
    "content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__stateOfIncorporation__name": "DELAWARE",
    "content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__countryOfIncorporation": "USA",
    "content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__countryOfIncorporation__name": "UNITED STATES",
    "content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__organizationalType": "PARTNERSHIP",
    "content__award__vendor__vendorSiteDetails__typeOfEducationalEntity": "\n              ",
    "content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__is1862LandGrantCollege": "false",
    "content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__is1890LandGrantCollege": "false",
    "content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__is1994LandGrantCollege": "false",
    "content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isHistoricallyBlackCollegeOrUniversity": "false",
    "content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isMinorityInstitution": "false",
    "content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isPrivateUniversityOrCollege": "false",
    "content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isSchoolOfForestry": "false",
    "content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isStateControlledInstitutionofHigherLearning": "false",
    "content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isTribalCollege": "false",
    "content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isVeterinaryCollege": "false",
    "content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isAlaskanNativeServicingInstitution": "false",
    "content__award__vendor__vendorSiteDetails__typeOfEducationalEntity__isNativeHawaiianServicingInstitution": "false",
    "content__award__vendor__vendorSiteDetails__vendorCertifications": "\n              ",
    "content__award__vendor__vendorSiteDetails__vendorCertifications__isDOTCertifiedDisadvantagedBusinessEnterprise": "false",
    "content__award__vendor__vendorSiteDetails__vendorCertifications__isSelfCertifiedSmallDisadvantagedBusiness": "false",
    "content__award__vendor__vendorSiteDetails__vendorCertifications__isSBACertifiedSmallDisadvantagedBusiness": "false",
    "content__award__vendor__vendorSiteDetails__vendorCertifications__isSBACertified8AProgramParticipant": "false",
    "content__award__vendor__vendorSiteDetails__vendorCertifications__isSelfCertifiedHUBZoneJointVenture": "false",
    "content__award__vendor__vendorSiteDetails__vendorCertifications__isSBACertifiedHUBZone": "false",
    "content__award__vendor__vendorSiteDetails__vendorCertifications__isSBACertified8AJointVenture": "false",
    "content__award__vendor__vendorSiteDetails__vendorLocation": "\n              ",
    "content__award__vendor__vendorSiteDetails__vendorLocation__streetAddress": "3737 MARSHALL AVE",
    "content__award__vendor__vendorSiteDetails__vendorLocation__city": "SAINT LOUIS",
    "content__award__vendor__vendorSiteDetails__vendorLocation__state": "MO",
    "content__award__vendor__vendorSiteDetails__vendorLocation__state__name": "MISSOURI",
    "content__award__vendor__vendorSiteDetails__vendorLocation__ZIPCode": "63119",
    "content__award__vendor__vendorSiteDetails__vendorLocation__ZIPCode__city": "SAINT LOUIS",
    "content__award__vendor__vendorSiteDetails__vendorLocation__countryCode": "USA",
    "content__award__vendor__vendorSiteDetails__vendorLocation__countryCode__name": "UNITED STATES",
    "content__award__vendor__vendorSiteDetails__vendorLocation__phoneNo": "9204618790",
    "content__award__vendor__vendorSiteDetails__vendorLocation__congressionalDistrictCode": "02",
    "content__award__vendor__vendorSiteDetails__vendorLocation__entityDataSource": "D&B",
    "content__award__vendor__vendorSiteDetails__vendorAlternateSiteCode": "63119",
    "content__award__vendor__vendorSiteDetails__entityIdentifiers": "\n              ",
    "content__award__vendor__vendorSiteDetails__entityIdentifiers__vendorUEIInformation": "\n                ",
    "content__award__vendor__vendorSiteDetails__entityIdentifiers__vendorUEIInformation__UEI": "QGUQWSU5AHB4",
    "content__award__vendor__vendorSiteDetails__entityIdentifiers__vendorUEIInformation__UEILegalBusinessName": "PERIMETER SOLUTIONS LP",
    "content__award__vendor__vendorSiteDetails__entityIdentifiers__vendorUEIInformation__ultimateParentUEI": "LBLLJKAVKL68",
    "content__award__vendor__vendorSiteDetails__entityIdentifiers__vendorUEIInformation__ultimateParentUEIName": "PERIMETER SOLUTIONS LP",
    "content__award__vendor__vendorSiteDetails__entityIdentifiers__cageCode": "1RKV8",
    "content__award__vendor__vendorSiteDetails__ccrRegistrationDetails": "\n              ",
    "content__award__vendor__vendorSiteDetails__ccrRegistrationDetails__registrationDate": "2000-09-16 00:00:00",
    "content__award__vendor__vendorSiteDetails__ccrRegistrationDetails__renewalDate": "2019-05-24 00:00:00",
    "content__award__vendor__contractingOfficerBusinessSizeDetermination": "O",
    "content__award__vendor__contractingOfficerBusinessSizeDetermination__description": "OTHER THAN SMALL BUSINESS",
    "content__award__placeOfPerformance": "\n          ",
    "content__award__placeOfPerformance__principalPlaceOfPerformance": "\n            ",
    "content__award__placeOfPerformance__principalPlaceOfPerformance__stateCode": "ID",
    "content__award__placeOfPerformance__principalPlaceOfPerformance__stateCode__name": "IDAHO",
    "content__award__placeOfPerformance__principalPlaceOfPerformance__countryCode": "USA",
    "content__award__placeOfPerformance__principalPlaceOfPerformance__countryCode__name": "UNITED STATES",
    "content__award__placeOfPerformance__placeOfPerformanceZIPCode": "837055354",
    "content__award__placeOfPerformance__placeOfPerformanceZIPCode__county": "ADA",
    "content__award__placeOfPerformance__placeOfPerformanceZIPCode__city": "BOISE",
    "content__award__placeOfPerformance__placeOfPerformanceCongressionalDistrict": "01",
    "content__award__competition": "\n          ",
    "content__award__competition__extentCompeted": "C",
    "content__award__competition__extentCompeted__description": "NOT COMPETED",
    "content__award__competition__solicitationProcedures": "SSS",
    "content__award__competition__solicitationProcedures__description": "ONLY ONE SOURCE",
    "content__award__competition__idvTypeOfSetAside": "NONE",
    "content__award__competition__idvTypeOfSetAside__description": "NO SET ASIDE USED.",
    "content__award__competition__typeOfSetAsideSource": "B",
    "content__award__competition__typeOfSetAsideSource__description": "IDC",
    "content__award__competition__evaluatedPreference": "NONE",
    "content__award__competition__evaluatedPreference__description": "NO PREFERENCE USED",
    "content__award__competition__reasonNotCompeted": "ONE",
    "content__award__competition__reasonNotCompeted__description": "ONLY ONE SOURCE-OTHER (FAR 6.302-1 OTHER)",
    "content__award__competition__idvNumberOfOffersReceived": "1",
    "content__award__competition__numberOfOffersSource": "B",
    "content__award__competition__numberOfOffersSource__description": "IDC",
    "content__award__competition__commercialItemAcquisitionProcedures": "A",
    "content__award__competition__commercialItemAcquisitionProcedures__description": "COMMERCIAL PRODUCTS/SERVICES",
    "content__award__competition__commercialItemTestProgram": "N",
    "content__award__competition__commercialItemTestProgram__description": "NO",
    "content__award__competition__A76Action": "N",
    "content__award__competition__A76Action__description": "NO",
    "content__award__competition__fedBizOpps": "Y",
    "content__award__competition__fedBizOpps__description": "YES",
    "content__award__competition__localAreaSetAside": "N",
    "content__award__competition__localAreaSetAside__description": "NO",
    "content__award__preferencePrograms": "\n          ",
    "content__award__preferencePrograms__subcontractPlan": "G",
    "content__award__preferencePrograms__subcontractPlan__description": "COMMERCIAL SUBCONTRACT PLAN ",
    "content__award__transactionInformation": "\n          ",
    "content__award__transactionInformation__createdBy": "LARRYROBILLARD@FS.FED.US",
    "content__award__transactionInformation__createdDate": "2023-02-07 14:27:43",
    "content__award__transactionInformation__lastModifiedBy": "LARRYROBILLARD@FS.FED.US",
    "content__award__transactionInformation__lastModifiedDate": "2023-02-07 15:12:28",
    "content__award__transactionInformation__status": "F",
    "content__award__transactionInformation__status__description": "FINAL",
    "content__award__transactionInformation__approvedBy": "LARRYROBILLARD@FS.FED.US",
    "content__award__transactionInformation__approvedDate": "2023-02-07 15:12:28",
    "content__award__transactionInformation__closedStatus": "N",
    "content__award__genericTags": "\n          ",
    "content__award__genericTags__genericStrings": "\n            ",
    "content__award__genericTags__genericStrings__genericString01": "2022-12-29 00:00:00",
    "content__award__genericTags__genericStrings__genericString02": "QGUQWSU5AHB4"