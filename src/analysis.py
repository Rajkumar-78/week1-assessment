from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
departments = pd.read_csv(ROOT / "data" / "departments.csv")
employees = pd.read_csv(ROOT / "data" / "employees.csv")

print("Departments:")
print(departments.to_string(index=False))
print(f"\\nDepartment count: {len(departments)}")
print(f"Total department budget: {departments['budget'].sum():,}")
print("\\nDepartments ranked by budget:")
print(departments.sort_values("budget", ascending=False).to_string(index=False))

print("\\nEmployees by department:")
if "department" in employees.columns:
    print(employees.groupby("department").size().rename("employee_count"))
else:
    print("No 'department' column found in employees.csv.")
if "city" in employees.columns:
    print("\\nEmployees by city:")
    print(employees.groupby("city").size().rename("employee_count"))
