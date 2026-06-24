import pandas as pd
from pathlib import Path


raw_path = Path("data/raw")
processed_path = Path("data/processed")


# Load NAV data
nav = pd.read_csv(raw_path / "02_nav_history.csv")

print("Before cleaning:")
print(nav.head())
print(nav.dtypes)


# Date conversion
nav["date"] = pd.to_datetime(nav["date"], errors="coerce")


# Sort
nav = nav.sort_values(
    ["amfi_code", "date"]
)


# Remove duplicates
nav = nav.drop_duplicates()


# Remove invalid NAV
nav = nav[nav["nav"] > 0]


# Save cleaned file
nav.to_csv(
    processed_path / "clean_nav_history.csv",
    index=False
)


print("NAV cleaning completed")
print(nav.shape)
# Load transactions data

transactions = pd.read_csv(
    raw_path / "08_investor_transactions.csv"
)

print(transactions.head())
print(transactions.dtypes)


# Standardize transaction type

transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.upper()
    .str.strip()
)


# Validate amount

transactions = transactions[
    transactions["amount_inr"] > 0
]


# Date format

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"],
    errors="coerce"
)


# Check KYC values

print(
    transactions["kyc_status"].unique()
)


# Remove duplicates

transactions = transactions.drop_duplicates()


# Save cleaned file

transactions.to_csv(
    processed_path / "clean_investor_transactions.csv",
    index=False
)


print("Transaction cleaning completed")
print(transactions.shape)

# Load scheme performance data

performance = pd.read_csv(
    raw_path / "07_scheme_performance.csv"
)

print(performance.head())
print(performance.dtypes)


# Convert numeric columns

numeric_cols = performance.select_dtypes(
    include="number"
).columns

for col in numeric_cols:
    performance[col] = pd.to_numeric(
        performance[col],
        errors="coerce"
    )


# Check missing numeric values

print("Missing values:")
print(performance.isnull().sum())


# Expense ratio validation

if "expense_ratio_pct" in performance.columns:

    invalid_expense = performance[
        (performance["expense_ratio_pct"] < 0.1) |
        (performance["expense_ratio_pct"] > 2.5)
    ]

    print("Invalid expense ratio rows:")
    print(invalid_expense)


# Remove duplicates

performance = performance.drop_duplicates()


# Save cleaned file

performance.to_csv(
    processed_path / "clean_scheme_performance.csv",
    index=False
)


print("Performance cleaning completed")
print(performance.shape)