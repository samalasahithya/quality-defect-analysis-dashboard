# Quality Defect Analysis Dashboard

**Tools:** Power BI, Excel, PostgreSQL  
**Dataset:** Manufacturing Quality Control (Kaggle)

## Overview
Interactive Power BI dashboard analyzing 10,000+ manufacturing records 
to identify defect trends, top error categories, and quality KPIs 
across departments — inspired by real Amazon QA operations.

## What This Project Does
- Analyzes defect trends over time using line charts
- Identifies top error categories by department using bar charts
- Monitors quality KPIs using Power BI card visuals
- Calculates Error Rate % using DAX: 
  `Error Rate % = DIVIDE(SUM(defects), SUM(total_units)) * 100`

## Key Insights
- Identified top defect categories contributing to 80% of total errors
- Tracked monthly defect trends across departments
- Automated error rate calculation replacing manual reporting

## Files in This Repo
| File | Description |
|---|---|
| `csv.xlsx` | Cleaned dataset used for analysis |
| `Quality_Defect_Dashboard.pdf` | Exported Power BI dashboard |
| `dashboard_screenshot.png` | Dashboard preview |
| `import_data.py` | Python script to import data into PostgreSQL |

## Resume Line
*Developed a Quality Defect Analysis dashboard in Power BI analyzing 
10,000+ records, identifying top error categories and reducing manual 
reporting effort by 40%*
