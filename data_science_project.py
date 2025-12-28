# =====================================================
# EDA ON INDIAN DATA SCIENCE JOB MARKET
# =====================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

# =====================================================
# LOAD DATA
# =====================================================
df = pd.read_csv("jobs.csv")

print("Initial Shape:", df.shape)
print(df.info())
print(df.describe(include="all"))

# =====================================================
# DATA CLEANING
# =====================================================

df.drop_duplicates(inplace=True)
df.dropna(subset=["Job Title", "Location", "Experience", "Salary"], inplace=True)

# -------------------------------
# CLEAN SALARY
# -------------------------------
def clean_salary(salary):
    salary = str(salary).replace("₹", "").replace(",", "").strip()
    if "-" in salary:
        low, high = salary.split("-")
        return (int(low) + int(high)) / 2
    else:
        return int(salary)

df["Salary"] = df["Salary"].apply(clean_salary)

# -------------------------------
# CLEAN EXPERIENCE
# -------------------------------
def clean_experience(exp):
    exp = str(exp).lower().replace("years", "").replace("year", "").strip()
    if "-" in exp:
        low, high = exp.split("-")
        return (int(low) + int(high)) / 2
    else:
        return float(exp)

df["Experience"] = df["Experience"].apply(clean_experience)

# -------------------------------
# CLEAN LOCATION
# -------------------------------
df["Location"] = df["Location"].str.strip().str.title()

print("Cleaned Shape:", df.shape)

# =====================================================
# EDA
# =====================================================

plt.figure()
df["Location"].value_counts().head(10).plot(kind="bar")
plt.title("Top Hiring Cities")
plt.xlabel("City")
plt.ylabel("Jobs")
plt.show()

plt.figure()
df["Job Title"].value_counts().head(10).plot(kind="bar")
plt.title("Top Job Roles")
plt.xlabel("Role")
plt.ylabel("Count")
plt.show()

plt.figure()
plt.hist(df["Salary"], bins=20)
plt.title("Salary Distribution")
plt.xlabel("Salary (INR)")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.scatter(df["Experience"], df["Salary"])
plt.title("Salary vs Experience")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary (INR)")
plt.show()

plt.figure()
df.groupby("Experience")["Salary"].mean().plot()
plt.title("Average Salary by Experience")
plt.xlabel("Experience")
plt.ylabel("Average Salary")
plt.show()

# =====================================================
# SAVE CLEAN DATA
# =====================================================
df.to_csv("cleaned_jobs.csv", index=False)
print("Cleaned data saved successfully.")
