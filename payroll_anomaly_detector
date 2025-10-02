# Author: Adeoluwa (Ade) Olateru-Olagbegi
# Project: Payroll Anomaly Detector
# Date: 08/18/2025
# Description: This program analyzes payroll data to calculate gross pay, 
# detect anomalies (overworked hours, duplicate employees, or unusual rates), 
# and exports results into an Excel report with detailed logs and flagged issues.

import pandas as pd

def analyze_payroll(input_file, output_file):
    """
    Reads a payroll CSV file, calculates gross pay, checks for anomalies,
    and saves both the full dataset and anomalies into an Excel file.
    """
    df = pd.read_csv(input_file)

    # Calculate gross pay for each employee
    df["Gross_Pay"] = df["Hours_Worked"] * df["Hourly_Rate"]

    # Collect anomalies
    anomalies = []

    # Rule 1: Employees with more than 60 hours a week
    anomalies.append(df[df["Hours_Worked"] > 60])

    # Rule 2: Hourly rate higher than $100 (suspicious)
    anomalies.append(df[df["Hourly_Rate"] > 100])

    # Rule 3: Duplicate employee IDs
    anomalies.append(df[df.duplicated("Employee_ID", keep=False)])

    # Combine all anomalies and remove duplicates
    anomaly_report = pd.concat(anomalies).drop_duplicates()

    # Save to Excel with two sheets: Full Data + Anomalies
    with pd.ExcelWriter(output_file) as writer:
        df.to_excel(writer, sheet_name="Payroll Data", index=False)
        anomaly_report.to_excel(writer, sheet_name="Anomalies", index=False)

    return anomaly_report


# Test
sample_payroll = {
    "Employee_ID": [201, 202, 203, 203, 204],
    "Name": ["Tola Adebayo", "Amina Bello", "Chike Nwosu", "Chike Nwosu", "Ngozi Okeke"],
    "Department": ["IT", "Finance", "IT", "IT", "HR"],
    "Hours_Worked": [40, 65, 38, 38, 45],
    "Hourly_Rate": [25, 30, 120, 120, 28]
}
pd.DataFrame(sample_payroll).to_csv("payroll_with_anomalies.csv", index=False)

anomalies = analyze_payroll("payroll_with_anomalies.csv", "payroll_anomalies.xlsx")
print("Detected Payroll Anomalies:\n", anomalies)
