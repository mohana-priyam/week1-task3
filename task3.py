import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Create output folder for charts
Path("output").mkdir(exist_ok=True)

# 4 students x 3 subjects
marks = np.array([
    [80, 75, 90],
    [65, 70, 72],
    [92, 88, 95],
    [55, 60, 58]
])

print("Shape:", marks.shape)
print("Student averages:", marks.mean(axis=1))
print("Subject averages:", marks.mean(axis=0))

# Add 5 grace marks to every subject using broadcasting
grace_marks = marks + 5
print("Marks after grace marks:\n", grace_marks)

# Weighted score: 50% subject 1, 30% subject 2, 20% subject 3
weights = np.array([0.5, 0.3, 0.2])
weighted_scores = np.dot(grace_marks, weights)

print("Weighted scores:", weighted_scores)

# Load employees.csv
df = pd.read_csv("employees.csv")
print("Column names:", df.columns.tolist())
print(df.head())

print("\n--- DataFrame info ---")
df.info()

print("\n--- Description ---")
print(df.describe())

# loc: select rows by condition and columns by name
print("\n--- Chennai employees ---")
print(df.loc[df["city"] == "Chennai", ["name", "salary"]])

# iloc: select rows and columns by position
print("\n--- First 3 rows ---")
print(df.iloc[:3, :])

# Filtering
print("\n--- Employees with salary above 50000 ---")
print(df.loc[df["salary"] > 50000, ["name", "salary"]])

print("\nMissing salaries before cleaning:", df["salary"].isna().sum())
print("Duplicate rows before cleaning:", df.duplicated().sum())

# Correct column types
df["id"] = pd.to_numeric(df["id"], errors="raise").astype(int)
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

# Fill missing salaries using the median of available salaries
median_salary = df["salary"].median()
df["salary"] = df["salary"].fillna(median_salary)

# Remove duplicate rows
df = df.drop_duplicates().copy()

print("Median salary used:", median_salary)
print("Missing salaries after cleaning:", df["salary"].isna().sum())
print("Duplicate rows after cleaning:", df.duplicated().sum())
print("\nCleaned employee data:")
print(df.to_string(index=False))

# Headcount, average salary and maximum salary
summary = df.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
).reset_index()

print("\n--- Department summary ---")
print(summary.to_string(index=False))

from pathlib import Path
import pandas as pd

file_path = Path(__file__).parent / "departments.csv"
departments = pd.read_csv(file_path)

print("\n--- Departments Data ---")
print(departments)

print("Departments columns:", departments.columns.tolist())
print("Summary columns:", summary.columns.tolist())

print("\nDepartments preview:")
print(departments.head())

print("\nSummary preview:")
print(summary.head())

# Inner join: only matching departments
print("Departments columns:", departments.columns.tolist())
print("Summary columns:", summary.columns.tolist())
inner_join = pd.merge(
    departments,
    summary,
    left_on="department_name",
    right_on="department",
    how="inner"
)

print("\n--- Inner Join ---")
print(inner_join)
# Read departments.csv
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent

departments = pd.read_csv(BASE_DIR / "departments.csv")
departments.columns = departments.columns.str.strip()

# Inner join
inner_join = pd.merge(
    departments,
    summary,
    left_on="department_name",
    right_on="department",
    how="inner"
)

print("\nInner Join:")
print(inner_join)

# Left join
left_join = pd.merge(
    departments,
    summary,
    left_on="department_name",
    right_on="department",
    how="left"
)

print("\nLeft Join:")
print(left_join)

# Outer join
outer_join = pd.merge(
    departments,
    summary,
    left_on="department_name",
    right_on="department",
    how="outer",
    indicator=True
)

print("\nOuter Join:")
print(outer_join)

# Departments with no employees
no_employees = outer_join.loc[
    outer_join["headcount"].isna(),
    "department_name"
].tolist()

print("\nDepartments with no employees:", no_employees)

# Left join: all departments from departments.csv

left_join = pd.merge(
    departments,
    summary,
    left_on="department_name",
    right_on="department",
    how="left"
)

print("\nLeft Join:")
print(left_join)

# Outer join: all departments from both DataFrames

# Department joins - final corrected version

# Remove spaces from column names
departments.columns = departments.columns.str.strip()
summary.columns = summary.columns.str.strip()

# Inner join
inner_join = pd.merge(
    departments,
    summary,
    left_on="department_name",
    right_on="department",
    how="inner"
)
print("\nInner Join:")
print(inner_join)

# Left join
left_join = pd.merge(
    departments,
    summary,
    left_on="department_name",
    right_on="department",
    how="left"
)
print("\nLeft Join:")
print(left_join)

# Outer join
outer_join = pd.merge(
    departments,
    summary,
    left_on="department_name",
    right_on="department",
    how="outer",
    indicator=True
)
print("\nOuter Join:")
print(outer_join)

# Departments with no employees
no_employees = outer_join.loc[
    outer_join["headcount"].isna(),
    "department_name"
].dropna().tolist()

print("\nDepartments with no employees:", no_employees)


# Inner join
inner_join = pd.merge(
    departments, summary,
    left_on="department_name",
    right_on="department",
    how="inner"
)

# Left join
left_join = pd.merge(
    departments, summary,
    left_on="department_name",
    right_on="department",
    how="left"
)

# Outer join
outer_join = pd.merge(
    departments, summary,
    left_on="department_name",
    right_on="department",
    how="outer",
    indicator=True
)

# Departments without employees
no_employees = outer_join.loc[
    outer_join["headcount"].isna(),
    "department_name"
].dropna().tolist()

print("Departments with no employees:", no_employees)

print("\n--- Inner join ---")
print(
    inner_join[
        ["department_name", "location", "headcount"]
    ].to_string(index=False)
)

print("\n--- Left join ---")
print(
    left_join[
        ["department_name", "location", "headcount"]
    ].to_string(index=False)
)

print(
    outer_join[
        ["department_name", "location", "headcount", "_merge"]
    ].to_string(index=False)
)

# Identify departments without employees
no_employees = outer_join.loc[
    outer_join["headcount"].isna(), "department"
].tolist()

print("Departments with no employees:", no_employees)

plt.figure(figsize=(8, 5))
plt.bar(summary["department"], summary["average_salary"], label="Average salary")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend()
plt.tight_layout()
plt.savefig("output/bar_chart.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.hist(df["salary"], bins=5, edgecolor="black", label="Employee salaries")

plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.legend()
plt.tight_layout()
plt.savefig("output/histogram.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.scatter(df["id"], df["salary"], label="Employees")

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig("output/scatter_plot.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.plot(
    summary["department"],
    summary["average_salary"],
    marker="o",
    label="Average salary"
)

plt.title("Department Average Salary Trend")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend()
plt.tight_layout()
plt.savefig("output/line_chart.png")
plt.close()

print("\nAll four charts saved successfully.")

import pandas as pd

df = pd.read_csv("employees.csv")

print("\n--- DataFrame info ---")
df.info()

print("\n--- Description ---")
print(df.describe(include="all"))

print("\n--- Chennai employees ---")
print(df.loc[df["city"] == "Chennai", ["name", "salary"]])
import pandas as pd
from pathlib import Path

file_path = Path(__file__).parent / "employees.csv"

df = pd.read_csv(file_path)

# Remove accidental spaces from column names
df.columns = df.columns.str.strip()

print("Columns:", df.columns.tolist())
print("\nEmployee data:")
print(df)

print("\n--- Chennai employees ---")
print(df.loc[
    df["city"].astype(str).str.strip().str.lower() == "chennai",
    ["name", "salary"]
])
from pathlib import Path
import pandas as pd

# Read CSV files from the folder containing task3.py
BASE_DIR = Path(__file__).resolve().parent

departments = pd.read_csv(
    BASE_DIR / "departments.csv",
    skipinitialspace=True
)

# Remove unwanted spaces from column names
departments.columns = departments.columns.str.strip()

print("Department columns:", departments.columns.tolist())

# Check the summary DataFrame too
print("Summary columns:", summary.columns.tolist())

# Perform joins
inner_join = pd.merge(
    departments,
    summary,
    left_on="department_name",
    right_on="department",
    how="inner"
)# Left join
left_join = pd.merge(
    departments, summary,
    left_on="department_name",
    right_on="department",
    how="left"
)

# Outer join
outer_join = pd.merge(
    departments, summary,
    left_on="department_name",
    right_on="department",
    how="outer",
    indicator=True
)

print("\n--- Inner join ---")
print(inner_join)

print("\n--- Left join ---")
print(left_join)

print("\n--- Outer join ---")
print(outer_join)

# Find departments with no employees
no_employees = outer_join.loc[
    outer_join["headcount"].isna(), "department"
].tolist()

print("\nDepartments with no employees:", no_employees)
summary = df.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
).reset_index()

# Department joins - corrected code

# Remove extra spaces from column names
departments.columns = departments.columns.str.strip()
summary.columns = summary.columns.str.strip()

# Inner join
inner_join = pd.merge(
    departments,
    summary,
    left_on="department_name",
    right_on="department",
    how="inner"
)
print("\nInner Join:")
print(inner_join)

# Left join
left_join = pd.merge(
    departments,
    summary,
    left_on="department_name",
    right_on="department",
    how="left"
)
print("\nLeft Join:")
print(left_join)

# Outer join
outer_join = pd.merge(
    departments,
    summary,
    left_on="department_name",
    right_on="department",
    how="outer",
    indicator=True
)
print("\nOuter Join:")
print(outer_join)

# Departments without employees
no_employees = outer_join.loc[
    outer_join["headcount"].isna(),
    "department_name"
].dropna().tolist()

print("Departments with no employees:", no_employees)