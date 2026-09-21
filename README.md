# Hospital Patient Care Analytics Pipeline

## Project Overview

The Hospital Patient Care Analytics Pipeline is an end-to-end Data Engineering project that demonstrates how hospital patient and appointment data can be extracted, transformed, validated, and loaded into a MySQL database.

## Objectives

* Extract patient and appointment data from CSV files.
* Clean and transform data using Python and Pandas.
* Validate data quality and consistency.
* Store cleaned data in MySQL tables.
* Automate the ETL workflow using Python.

## Technologies Used

* Python
* Pandas
* MySQL
* MySQL Connector
* CSV
* Git and GitHub

## Project Structure

```text
Hospital_Patient_Care_Analytics_Pipeline/
├── data/
│   ├── hospital_data.csv
│   └── output/
│       ├── clean_patients.csv
│       └── clean_appointments.csv
├── config.py
├── extract.py
├── transform.py
├── validate.py
├── load.py
├── pipeline.py
└── README.md
```

## ETL Workflow

1. **Extract:** Read hospital data from the CSV file and separate patient and appointment records.
2. **Transform:** Clean text fields, convert dates and numeric values, and prepare the data.
3. **Validate:** Check required fields, duplicate IDs, valid ages, wait times, and patient references.
4. **Save:** Store cleaned patient and appointment data as CSV files.
5. **Load:** Insert the cleaned records into MySQL database tables.

## How to Run the Project

### 1. Install dependencies

```bash
pip install pandas mysql-connector-python
```

### 2. Configure MySQL

Create a MySQL database named `hospital_analytics` and update the database credentials in `config.py`.

### 3. Run the pipeline

```bash
py pipeline.py
```

## Expected Output

The pipeline extracts, transforms, and validates the hospital data, saves the cleaned CSV files, and loads the records into MySQL.

## Learning Outcomes

* Understanding the ETL process.
* Working with CSV files using Pandas.
* Performing data cleaning and validation.
* Connecting Python applications to MySQL.
* Organizing and running a data engineering pipeline.

## Note

This project uses sample hospital data for learning and demonstration purposes.
