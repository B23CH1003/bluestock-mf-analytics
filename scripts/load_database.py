import pandas as pd
from sqlalchemy import create_engine


# Database create
engine = create_engine("sqlite:///bluestock_mf.db")


# Load cleaned files

nav = pd.read_csv(
    "data/processed/clean_nav_history.csv"
)

transactions = pd.read_csv(
    "data/processed/clean_investor_transactions.csv"
)

performance = pd.read_csv(
    "data/processed/clean_scheme_performance.csv"
)


# Load into SQLite

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)


transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)


performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)


print("Database loaded successfully")
from sqlalchemy import text


with engine.connect() as conn:

    for table in [
        "fact_nav",
        "fact_transactions",
        "fact_performance"
    ]:

        result = conn.execute(
            text(f"SELECT COUNT(*) FROM {table}")
        )

        print(
            table,
            result.fetchone()[0]
        )