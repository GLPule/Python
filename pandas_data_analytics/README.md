# Pandas Data Analytics

This project folder contains a practical introduction to data analysis with Python and pandas. It focuses on core pandas concepts such as Series, DataFrames, reading and writing CSV/JSON/Excel files, and basic data manipulation.

## Project purpose

The notebook in this folder demonstrates how to:

- Create and work with pandas Series
- Build and manipulate DataFrames
- Read data from CSV, JSON, and Excel files
- Inspect data types and structure
- Export data back to different formats
- Work with sample sales data

## Files included

- `main.ipynb` — main notebook with pandas examples and exercises
- `data.csv` — sample CSV dataset
- `data1.csv` — additional sample CSV dataset
- `sales_example.csv` — sales dataset used for examples
- `sales_example.json` — sales data exported in JSON format
- `sales_example.xlsx` — sales data exported in Excel format
- `data.xlsx` — Excel sample data

## Topics covered

### 1. Series

Examples showing how to:

- create Series from lists and dictionaries
- access values using labels
- check shape and length

### 2. DataFrames

Examples showing how to:

- create DataFrames from dictionaries and lists
- add columns and rows
- create empty DataFrames
- select rows and columns

### 3. CSV handling

Examples showing how to:

- read CSV files with pandas
- inspect data with `info()`
- parse date columns
- export DataFrames to CSV

### 4. JSON handling

Examples showing how to:

- create DataFrames from JSON-like data
- load JSON files with pandas
- check column data types

### 5. Excel handling

Examples showing how to:

- read Excel workbooks
- parse date columns
- load data from sheet-based files

## Requirements

Make sure you have Python installed with the following packages:

- pandas
- openpyxl (for Excel support)
- jupyter (optional, if you want to run the notebook interactively)

You can install them with:

```bash
pip install pandas openpyxl jupyter
```

## How to use

Open the notebook in Jupyter or VS Code:

```bash
jupyter notebook main.ipynb
```

Or open the notebook directly in VS Code's notebook viewer.

## Learning outcome

This folder is suitable for beginners learning:

- pandas basics
- tabular data analysis
- loading and saving common datasets
- data preparation for future analytics or machine learning projects

## Notes

This is a hands-on practice project focused on understanding the core pandas workflow used in real-world data analysis.
