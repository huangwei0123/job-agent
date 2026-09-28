import pandas as pd

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

    jobs = pd.concat(results)

    jobs = jobs.drop_duplicates(
        subset=["title", "company"]
    )

    jobs = enrich_dataframe(jobs)

    save_jobs(jobs)

    report = generate_report(jobs)

    report.to_csv(
        "daily_top_matches.csv",
        index=False
    )

    print()
    print("Saved daily_top_matches.csv")


if __name__ == "__main__":
    main()
