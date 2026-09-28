from sqlalchemy import create_engine

DB = "sqlite:///data/jobs.db"

engine = create_engine(DB)


def save_jobs(df):

    df.to_sql(
        "jobs",
        engine,
        if_exists="append",
        index=False
    )
