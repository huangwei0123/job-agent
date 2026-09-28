import json

PROFILE_FILE = "data/resume_profile.json"

with open(PROFILE_FILE) as f:
    PROFILE = json.load(f)

KEYWORDS = PROFILE["skills"]


def score_job(description):

    if description is None:
        return 0

    text = description.lower()

    score = 0

    for keyword, weight in KEYWORDS.items():

        if keyword.lower() in text:

            score += weight

    return score


def enrich_dataframe(df):

    scores = []

    for _, row in df.iterrows():

        description = str(row.get("description", ""))

        scores.append(score_job(description))

    df["score"] = scores

    return df
