from config import MINIMUM_SCORE


def generate_report(df):

    good = df[df["score"] >= MINIMUM_SCORE]

    good = good.sort_values(
        by="score",
        ascending=False
    )

    top = good.head(25)

    print("")
    print("=" * 90)
    print("TOP MATCHES")
    print("=" * 90)

    for _, row in top.iterrows():

        print()
        print("TITLE:", row.get("title"))
        print("COMPANY:", row.get("company"))
        print("SCORE:", row.get("score"))
        print("LOCATION:", row.get("location"))
        print("URL:", row.get("job_url"))
        print("-" * 90)

    return top
