# OTTO Data Engineering Assignment

## Overview

This project implements a simple data pipeline to generate a **revenue** table for January 2025 based on the provided **product** and **sales** data.

The final table is designed to support Power BI reporting by ensuring that **every product appears for every day in January 2025**, even if no sales occurred on a particular day.

---

## Tech Stack

- Python 3.x
- SQLite
- SQL
- Pandas

---

## Project Structure

```
otto-data-pipeline/
│
├── data/
│   ├── product.csv
│   └── sales.csv
│
├── sql/
│   └── revenue.sql
│
├── src/
│   └── pipeline.py
│
├── product_sales.db
├── requirements.txt
└── README.md
```

---

## Files Description

### `data/`

Contains the source CSV files provided with the assignment.

- `product.csv`
- `sales.csv`

---

### `product_sales.db`

SQLite database provided as part of the assignment.

Contains the following tables:

- `product`
- `sales`

The solution creates an additional table:

- `revenue`

---

### `sql/revenue.sql`

Contains the complete SQL transformation logic.

The SQL performs the following steps:

1. Generates all dates for January 2025.
2. Creates every product-date combination using a **CROSS JOIN**.
3. Joins sales data using a **LEFT JOIN**.
4. Aggregates multiple sales for the same product and day.
5. Replaces missing sales with `0`.
6. Calculates revenue.

---

### `src/pipeline.py`

Acts as the orchestration layer.

Responsibilities:

- Connects to the SQLite database.
- Executes the SQL script.
- Creates the `revenue` table.
- Displays sample output for verification.

---

## Revenue Calculation

The final revenue table contains the following columns:

| Column | Description |
|----------|-------------|
| sku_id | Product identifier |
| date_id | Date in January 2025 |
| price | Product price |
| sales | Total units sold on that day |
| revenue | Price × Sales |

Revenue is calculated as:

```
Revenue = Price × Sales
```

Products without sales are included with:

```
Sales = 0
Revenue = 0
```

---

## SQL Logic

The transformation follows these steps:

1. Generate a calendar for January 2025.
2. Create every possible combination of:
   - Product
   - Date
3. Left join the sales table.
4. Aggregate daily sales using `SUM(sales)`.
5. Replace NULL values using `COALESCE`.
6. Calculate revenue.

This ensures one record per product per day.

---

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Execute the pipeline

```bash
python src/pipeline.py
```

---

## Expected Output

The pipeline creates a new table named:

```
revenue
```

Expected number of rows:

```
1000 Products × 31 Days = 31,000 Records
```

---

## Assumptions

- Product price is sourced from the `product` table.
- Revenue is calculated as `Price × Sales`.
- Multiple sales for the same product on the same day are aggregated using `SUM(sales)`.
- Only January 2025 data is included.
- Products with no sales on a given day are included with zero sales and zero revenue.

---

## Future Improvements

Given more time, the following enhancements could be added:

- Logging
- Configuration file for database paths
- Data quality validations
- Unit tests
- Parameterized date range
- Support for BigQuery instead of SQLite