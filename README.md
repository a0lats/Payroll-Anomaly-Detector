# Payroll Anomaly Detector

## Description
This project analyzes payroll data stored in CSV files and automatically identifies irregularities.  
It calculates gross pay for each employee and detects anomalies such as:
- Employees working more than 60 hours per week  
- Suspiciously high hourly rates (>$100/hr)  
- Duplicate employee IDs  

The results are exported into an Excel file with two sheets:
- **Payroll Data** (full dataset)  
- **Anomalies** (flagged records only)  

This tool reduces manual payroll checking and makes auditing faster and more reliable.

---

## Technologies
- Python  
- Pandas  
- Excel (via openpyxl)

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/a0lats/Payroll-Anomaly-Detector.git
   cd Payroll-Anomaly-Detector
