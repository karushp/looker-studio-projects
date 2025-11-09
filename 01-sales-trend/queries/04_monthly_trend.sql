SELECT
  year,
  month_number,
  month_name,
  SUM(total_sales) AS monthly_sales
FROM `project_id.dataset.serialized_sales`
GROUP BY year, month_number, month_name
ORDER BY month_number, year;
