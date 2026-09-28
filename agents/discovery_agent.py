from jobspy import scrape_jobs
from config import SEARCH_TERMS
from config import LOCATION
from config import RESULTS_WANTED

def fetch_jobs():

    all_jobs = []

    for term in SEARCH_TERMS:

        print(f"Searching: {term}")

        try:

            jobs = scrape_jobs(
                site_name=[
                    "linkedin",
                    "indeed"
                ],
                search_term=term,
                location=LOCATION,
                results_wanted=RESULTS_WANTED,
                hours_old=168
            )

            if jobs is not None:
                all_jobs.append(jobs)

        except Exception as ex:
            print(ex)

    return all_jobs
