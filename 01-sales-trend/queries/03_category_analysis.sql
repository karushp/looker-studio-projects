SELECT
  region,
  category,
  SUM(total_sales) AS region_sales
FROM `project_id.dataset.serialized_sales`
GROUP BY region, category
ORDER BY region, region_sales DESC;
