import json

PROFILE_FILE = "data/resume_profile.json"

with open(PROFILE_FILE) as f:
    PROFILE = json.load(f)

KEYWORDS = PROFILE.get("skills", {})

# Define title keyword bonuses (adjust weights or words as needed)
TITLE_BOOSTS = {
    "principal": 25,
    "scientist": 20,
    "research": 15,
    "machine learning": 20,
    "artificial intelligence": 20,
    "ai": 15,
    "computational": 15,
    "weather": 20,
    "climate": 20
}


def score_job(row):
    title = str(row.get("title", "")).lower()
    description = str(row.get("description", "")).lower()

    text = description

    score = 0

    # Score based on skill keywords present in description
    for keyword, weight in KEYWORDS.items():
        if keyword.lower() in text:
            score += weight

    # Score based on title bonuses
    for word, bonus in TITLE_BOOSTS.items():
        if word in title:
            score += bonus

    return score


def enrich_dataframe(df):
    scores = []

    for _, row in df.iterrows():
        # Pass the entire row to score_job instead of just description
        scores.append(score_job(row))

    df["score"] = scores

    return df
