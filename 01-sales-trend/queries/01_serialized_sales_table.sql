CREATE OR REPLACE TABLE ecom_data.sales_serialized AS
SELECT
  '2024' AS year,
  date,
  product_id,
  category,
  units_sold,
  unit_price,
  value,
  region,
  channel
FROM `ecom_data.sales_2024`

UNION ALL

SELECT
  '2025' AS year,
  date,
  product_id,
  category,
  units_sold,
  unit_price,
  value,
  region,
  channel
FROM `ecom_data.sales_2025`;