# HR Employee Attrition Analysis
An end-to-end data analysis project examining employee attrition using Python, SQL, Excel, and Power BI on the IBM HR Analytics dataset (1,470 employees).

## 📊 Project Overview
This project identifies which employee segments are most likely to leave a company
and provides data-driven recommendations for HR retention strategy.

## 🛠️ Tools & Technologies
- **Python** (Pandas, Matplotlib) — data cleaning and exploratory data analysis
- **MySQL** (SQLAlchemy) — database queries and window functions
- **Excel** (Power Query, PivotTables) — data validation and summary reporting
- **Power BI** — interactive dashboard with DAX measures

## 🔑 Key Findings
- Overall attrition rate: **16.12%**
- Employees working overtime have **3x higher attrition** (30.5% vs 10.4%)
- **Sales Representatives** have the highest attrition rate at **39.76%**
- Sales Reps working overtime show a combined **66.7% attrition rate**

## 📁 Repository Structure
├── Python/
│   ├── main.py                    # EDA script
│   └── load_to_mysql.py           # Data loading script
├── sql/
│   └── HR_Attrition.sql           # Business question queries
├── excel/
│   └── HR_Attrition.xlsx          # PivotTable analysis
├── power bi/
│   └── HR_Attrition_Dashboard.pbix
├── screenshot/
│   └── (dashboard and chart images)
└── README.md

## 💡 Business Recommendation
HR should prioritize retention interventions — workload management, overtime reduction,
career development — for Sales Representative and overtime-heavy roles rather than
applying uniform, company-wide retention policies.

## 📌 Dataset Source
[IBM HR Analytics Employee Attrition & Performance (Kaggle)](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
