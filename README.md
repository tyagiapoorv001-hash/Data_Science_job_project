# Indian Data Science Job Market EDA

This project performs exploratory data analysis on Indian data science job listings to understand salary trends, experience requirements, common job roles, and top hiring locations.

## Project Overview

The analysis focuses on practical job-market questions:

- Which cities have the most data science openings?
- Which job titles appear most often?
- How does salary change with experience?
- What skills are common in the listings?

## Project Structure

```text
Data_Science_job_project/
|-- jobs.csv
|-- data_science_project.py
|-- requirements.txt
`-- README.md
```

## Dataset

The dataset includes job title, company, location, required experience, salary range, and skills.

## Key Insights

- Bangalore and Hyderabad have the highest number of data science job openings.
- Data Analyst and Data Scientist are common job roles.
- Salary increases noticeably after 3+ years of experience.
- Entry-level salaries are mostly below 8 LPA in the sample dataset.

## How to Run

```bash
pip install -r requirements.txt
python data_science_project.py
```

The script cleans the dataset, creates exploratory charts, and saves `cleaned_jobs.csv`.

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
