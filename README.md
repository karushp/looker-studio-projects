# Looker Studio Projects

This repository showcases my **Looker Studio** projects and data visualization work. Each project demonstrates different techniques for data modeling, transformation, and visualization using **BigQuery** and **Looker Studio**.

Projects will be added to this repository as they are completed in Looker Studio.

---

## 📁 Projects

### 01-sales-trend: Sales Trend Analysis (2024 vs 2025)

A comprehensive project demonstrating how to model, serialize, and visualize sales data across multiple years. This project solves the common challenge of comparing year-over-year trends by transforming raw yearly data into a unified dataset that allows dynamic comparisons in a single dashboard.

**Key Highlights:**
- Combines multiple year tables (2024 & 2025) into one serialized dataset in BigQuery
- Enables year-over-year trend visualization without overlaying separate dashboards
- Includes data generation scripts, SQL transformation queries, and dashboard visualizations
- Demonstrates best practices for multi-year data serialization and aggregation

**Tech Stack:** BigQuery, Looker Studio, Python, SQL

[View Project Details →](01-sales-trend/README.md)

---

### 02-CRM-Reporting: CRM Reporting Dashboard

A sample dashboard project demonstrating automated CRM data extraction and linking BigQuery data to Looker Studio. This project showcases how to streamline CRM reporting workflows by connecting CRM systems to BigQuery and visualizing the data in Looker Studio.

**Key Highlights:**
- Automated CRM data extraction workflows
- Data transformation and storage in BigQuery
- Real-time dashboard visualization in Looker Studio
- Sample POS (Point of Sale) data integration
- Multi-page dashboard with comprehensive CRM metrics

**Tech Stack:** CRM Systems, BigQuery, Looker Studio, Data Automation

[View Project Details →](02-CRM-Reporting/README.md)

---

### 03-energy-consumption-analysis: Energy Consumption Analysis Dashboard

A comprehensive project demonstrating how to analyze and visualize building energy consumption patterns. This project showcases energy usage trends, environmental factor correlations, and occupancy pattern impacts to help optimize energy efficiency and reduce costs.

**Key Highlights:**
- Hourly energy consumption tracking with time series analysis
- Environmental factor correlation (temperature, humidity)
- Occupancy pattern analysis and its impact on energy usage
- HVAC and lighting usage optimization insights
- Renewable energy contribution tracking
- Multi-page dashboard with comprehensive energy metrics

**Tech Stack:** BigQuery, Looker Studio, Python, SQL

[View Project Details →](03-energy-consumption-analysis/README.md)

---

## 🛠️ Technical Stack

- **BigQuery** – Data storage, transformation, and SQL modeling
- **Looker Studio** – Dashboard creation and data visualization
- **Python** – Data generation and preprocessing scripts
- **SQL (BigQuery Standard SQL)** – Data preparation and aggregation

---

## 📝 Project Structure

Each project follows a consistent structure:
- `queries/` – SQL queries for BigQuery transformations (when applicable)
- `data/` or `sales_data/` – Sample data files and generation scripts
- `images/` – Dashboard and visualization previews
- `README.md` – Project-specific documentation
