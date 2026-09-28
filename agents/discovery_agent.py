import time

from jobspy import scrape_jobs
from config import SEARCH_TERMS
from config import LOCATION
from config import RESULTS_WANTED

def fetch_jobs():

    all_jobs = []

    for term in SEARCH_TERMS:

        print(f"Searching: {term}")

        start=time.time()

        print(f"\nSearching: {term}")

        try:

            jobs = scrape_jobs(
                site_name=[
                    "linkedin",
                    "indeed"
                ],
                search_term=term,
                location=LOCATION,
                results_wanted=RESULTS_WANTED,
                hours_old=48
            )

            if jobs is not None:
                all_jobs.append(jobs)

        except Exception as ex:
            print(ex)

        print(
            f"Finished {term} "
            f"in {time.time()-start:.2f} sec"
        )

    return all_jobs
