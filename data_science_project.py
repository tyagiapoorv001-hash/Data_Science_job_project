import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_theme()

df = pd.read_csv("jobs.csv")

print("Initial shape:", df.shape)
print(df.info())
print(df.describe(include="all"))

df.drop_duplicates(inplace=True)
df.dropna(subset=["Job Title", "Location", "Experience", "Salary"], inplace=True)


def clean_salary(salary):
    salary = str(salary).replace("INR", "").replace("Rs.", "").replace(",", "").strip()
    if "-" in salary:
        low, high = salary.split("-")
        return (int(low) + int(high)) / 2
    return int(salary)


def clean_experience(experience):
    experience = str(experience).lower().replace("years", "").replace("year", "").strip()
    if "-" in experience:
        low, high = experience.split("-")
        return (int(low) + int(high)) / 2
    return float(experience)


df["Salary"] = df["Salary"].apply(clean_salary)
df["Experience"] = df["Experience"].apply(clean_experience)
df["Location"] = df["Location"].str.strip().str.title()

print("Cleaned shape:", df.shape)

plt.figure()
df["Location"].value_counts().head(10).plot(kind="bar")
plt.title("Top Hiring Cities")
plt.xlabel("City")
plt.ylabel("Jobs")
plt.tight_layout()
plt.savefig("top_hiring_cities.png")

plt.figure()
df["Job Title"].value_counts().head(10).plot(kind="bar")
plt.title("Top Job Roles")
plt.xlabel("Role")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("top_job_roles.png")

plt.figure()
plt.hist(df["Salary"], bins=10)
plt.title("Salary Distribution")
plt.xlabel("Salary (INR)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("salary_distribution.png")

plt.figure()
plt.scatter(df["Experience"], df["Salary"])
plt.title("Salary vs Experience")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary (INR)")
plt.tight_layout()
plt.savefig("salary_vs_experience.png")

plt.figure()
df.groupby("Experience")["Salary"].mean().plot()
plt.title("Average Salary by Experience")
plt.xlabel("Experience")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.savefig("average_salary_by_experience.png")

df.to_csv("cleaned_jobs.csv", index=False)
print("Cleaned data saved successfully.")
