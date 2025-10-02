# Author: Adeoluwa (Ade) Olateru-Olagbegi
# Project: Smart Payroll Anomaly Detector
# Date: 08/18/2025
# Description: Enhances payroll processing by detecting anomalies (overpaid hours,
# duplicate entries, unusual rates). Exports flagged reports to Excel.

import pandas as pd

def analyze_payroll(input_file, output_file):
    df = pd.read_csv(input_file)

    # Calculate gross pay
    df["Gross_Pay"] = df["Hours_Worked"] * df["Hourly_Rate"]

    # Detect anomalies
    anomalies = []

    # Rule 1: Over 60 hours in a week
    anomalies.append(df[df["Hours_Worked"] > 60])

    # Rule 2: Hourly rate suspiciously high (> $100/hr)
    anomalies.append(df[df["Hourly_Rate"] > 100])

    # Rule 3: Duplicate Employee_ID
    anomalies.append(df[df.duplicated("Employee_ID", keep=False)])

    # Combine anomaly results
    anomaly_report = pd.concat(anomalies).drop_duplicates()

    # Export to Excel
    with pd.ExcelWriter(output_file) as writer:
        df.to_excel(writer, sheet_name="Payroll Data", index=False)
        anomaly_report.to_excel(writer, sheet_name="Anomalies", index=False)

    return anomaly_report


# -------------------------
# Test Run (Safe Demo)
# -------------------------
sample_payroll = {
    "Employee_ID": [201, 202, 203, 203, 204],
    "Name": ["John Doe", "Sarah Lee", "Mike Chan", "Mike Chan", "Jane Park"],
    "Department": ["IT", "Finance", "IT", "IT", "HR"],
    "Hours_Worked": [40, 65, 38, 38, 45],
    "Hourly_Rate": [25, 30, 120, 120, 28]
}
pd.DataFrame(sample_payroll).to_csv("payroll_with_anomalies.csv", index=False)

anomalies = analyze_payroll("payroll_with_anomalies.csv", "payroll_anomalies.xlsx")
print("Detected Payroll Anomalies:\n", anomalies)
# -------------------------
# Test Run (Safe Demo)
# -------------------------
sample_payroll = {
    "Employee_ID": [201, 202, 203, 203, 204],
    "Name": ["John Doe", "Sarah Lee", "Mike Chan", "Mike Chan", "Jane Park"],
    "Department": ["IT", "Finance", "IT", "IT", "HR"],
    "Hours_Worked": [40, 65, 38, 38, 45],
    "Hourly_Rate": [25, 30, 120, 120, 28]
}
import pandas as pd
pd.DataFrame(sample_payroll).to_csv("payroll_with_anomalies.csv", index=False)

anomalies = analyze_payroll("payroll_with_anomalies.csv", "payroll_anomalies.xlsx")
print("Detected Payroll Anomalies:\n", anomalies)