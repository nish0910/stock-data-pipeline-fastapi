# stock-data-pipeline-fastapi
End-to-end stock data pipeline using Python, FastAPI, MySQL, and Power BI dashboard.
# 📊 End-to-End Stock Data Pipeline with FastAPI & Power BI

## 🚀 Project Overview

This project implements an **end-to-end stock data pipeline** that fetches stock data from an external API, processes and transforms it using Python, stores it in a MySQL database, exposes the data through REST APIs using FastAPI, and visualizes insights using a Power BI dashboard.

The project demonstrates real-world **Data Engineering and Backend Development** concepts including ETL workflows, API integration, database management, and dashboard reporting.

---

## 🛠️ Tech Stack

### Programming & Backend
- Python
- FastAPI
- REST APIs

### Data Processing
- Pandas
- Requests

### Database
- MySQL
- SQL

### Data Visualization
- Power BI

### Automation
- Python Scheduler
- Windows Task Scheduler

---

## 🏗️ System Architecture


External API
↓
Data Ingestion (Python)
↓
Data Transformation (Pandas)
↓
MySQL Database
↓
FastAPI Backend
↓
Power BI Dashboard


---

## 📂 Project Structure


stock-data-pipeline/

├── app/
│ ├── api.py
│ ├── fetch_data.py
│ ├── transform_data.py
│
├── database/
│ ├── load_to_db.py
│ ├── create_tables.sql
│
├── scheduler/
│ ├── run_pipeline.py
│
├── dashboard/
│ ├── stock data dashboard.pbix
│
├── screenshots/
│ ├── dashboard_full.png
│ ├── price_trend.png
│ ├── kpi_cards.png
│
├── data/
│ ├── clean_stock_data.csv
| ├── raw_stock_data.csv

│
├── requirements.txt
├── README.md


---

## 🔄 Pipeline Workflow

### Step 1 — Data Ingestion
- Fetch stock data from external API
- Convert JSON response into structured data
- Save raw data to CSV

### Step 2 — Data Transformation
- Clean missing values
- Convert data types
- Sort and structure dataset
- Prepare data for database storage

### Step 3 — Data Storage
- Store processed data into MySQL database
- Use SQL queries for insertion

### Step 4 — API Development
- Build REST APIs using FastAPI
- Provide endpoints to query stock data
- Support filtering and aggregation

### Step 5 — Dashboard Visualization
- Load processed data into Power BI
- Create interactive charts and KPIs
- Display key business insights

---

## 🌐 FastAPI Endpoints

### Get All Records


GET /stocks


Returns latest stock records.

---

### Get Latest Record


GET /latest


Returns most recent stock entry.

---

### Get Statistics


GET /stats


Returns:

- Total Records  
- Average Close Price  
- Maximum Price  
- Minimum Price  

---

### Get Data by Date


GET /by-date/{date}


Example:


GET /by-date/2025-01-15


---

### Get Average Price


GET /average-price


Returns average open and close prices.

---

## 📊 Dashboard Features

The Power BI dashboard includes:

- 📈 Stock Closing Price Trend
- 📊 Monthly Volume Trend
- 📉 KPI Cards:
  - Average Close Price
  - Highest Price
  - Lowest Price
- 📋 Detailed Stock Data Table

---


## ⚙️ Installation Guide

### Step 1 — Clone Repository


git clone https://github.com/nish0910/stock-data-pipeline-fastapi.git

cd stock-data-pipeline-fastapi


---

### Step 2 — Create Virtual Environment


python -m venv venv

venv\Scripts\activate


---

### Step 3 — Install Dependencies


pip install -r requirements.txt


---

### Step 4 — Configure Database

Create MySQL database:


CREATE DATABASE stock_pipeline;


Run table creation script:


create_tables.sql


---

### Step 5 — Run Pipeline


python -m scheduler.run_pipeline


---

### Step 6 — Start FastAPI Server


python -m uvicorn app.api:app --reload


Open:


http://127.0.0.1:8000/docs


---

## 🔄 Automation

The pipeline can be automated using:

- Windows Task Scheduler
- Scheduled Python execution

This enables periodic data updates.

---

## 🎯 Key Features

✔ End-to-End Data Pipeline  
✔ API Integration  
✔ Data Transformation  
✔ Database Storage  
✔ REST API Backend  
✔ Automated Workflow  
✔ Interactive Dashboard  

---

## 🧠 Skills Demonstrated

- Python Programming
- API Development
- Data Engineering
- SQL & Database Management
- ETL Pipeline Design
- Data Visualization
- Backend System Design

---

## 👨‍💻 Author

**Nishchal Srivastava**

Senior Associate — IT Automation  
Aspiring Data Engineer | Backend Developer

---

## ⭐ Future Enhancements

- Implement cloud deployment (AWS / Azure)
- Add authentication to APIs
- Implement streaming pipelines
- Deploy dashboard to Power BI Service
