import pandas as pd
from datetime import datetime
from pathlib import Path

from agents.discovery_agent import fetch_jobs
from agents.matching_agent import enrich_dataframe
from agents.storage_agent import save_jobs
from agents.reporting_agent import generate_report


def main():
    print("Starting Job Search AI Agent")

    results = fetch_jobs()

    if len(results) == 0:
        print("No jobs found")
        return

    # jobs = pd.concat(results)
    valid_results = [
        df for df in results if not df.empty and not df.dropna(how="all").empty
    ]

    if valid_results:
        jobs = pd.concat(valid_results, ignore_index=True)
    else:
        print("No valid job data found.")
        return

    jobs = jobs.drop_duplicates(subset=["title", "company"])

    jobs = enrich_dataframe(jobs)

    jobs = jobs.drop_duplicates(subset=["job_url"])

    print(jobs.columns)
    print(jobs.head())

    save_jobs(jobs)

    report = generate_report(jobs)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")

    Path("reports").mkdir(exist_ok=True)

    filename = f"reports/daily_top_matches_{timestamp}.csv"

    report.to_csv(filename, index=False)

    htmlname = f"dashboard_{timestamp}.html"
    report.to_html(htmlname, escape=False)

    print()
    print(f"\nSaved {filename}")


if __name__ == "__main__":
    main()
