-- Preview 2024 sales data
SELECT *
FROM `project_id.dataset.sales_2024`
LIMIT 10;

-- Preview 2025 sales data
SELECT *
FROM `project_id.dataset.sales_2025`
LIMIT 10;

-- Compare schema between 2024 and 2025 tables
SELECT
  table_name,
  column_name,
  data_type
FROM `project_id.dataset.INFORMATION_SCHEMA.COLUMNS`
WHERE table_name IN ('sales_2024', 'sales_2025')
ORDER BY column_name;
