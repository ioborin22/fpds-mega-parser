# FPDS Analytics in ClickHouse

This database contains summary and analytical tables derived from the raw FPDS contracts stored in `fpds_clickhouse.raw_contracts`.

## 🔧 Structure

- `fpds_clickhouse.raw_contracts` – primary data source (JSON import)
- `fpds_analytics.*` – materialized analytics, updated in real-time via Materialized Views
- All analytics use `SummingMergeTree` and group logic for performance

---

## 📊 Table: `contract_type_summary`

Aggregated total contract counts per `contract_type`.

### Data Flow:

- A `MATERIALIZED VIEW` (`contract_type_summary_mv`) listens to inserts in `raw_contracts`
- Each new row increments `total` in `contract_type_summary`

### Schema:

| Column        | Type     | Description                |
|---------------|----------|----------------------------|
| contract_type | UInt8    | Contract type enum (1–4)   |
| total         | UInt64   | Total contracts of that type |

### Query Example:

```sql
SELECT 
  CASE contract_type
    WHEN 1 THEN 'AWARD'
    WHEN 2 THEN 'IDV'
    WHEN 3 THEN 'OTHERTRANSACTIONAWARD'
    WHEN 4 THEN 'OTHERTRANSACTIONIDV'
    ELSE 'UNKNOWN'
  END AS contract_type_label,
  SUM(total) AS total
FROM fpds_analytics.contract_type_summary
GROUP BY contract_type
ORDER BY total DESC;
