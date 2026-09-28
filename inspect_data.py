import pandas as pd

df = pd.read_csv("daily_top_matches.csv")

cols = [
    "title",
    "company",
    "location",
    "score",
    "job_url"
]

print(df[cols].head(20).to_string())
