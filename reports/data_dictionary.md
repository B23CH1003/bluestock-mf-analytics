# Data Dictionary - Mutual Fund Analytics


## fact_nav

| Column | Data Type | Description |
|---|---|---|
| amfi_code | Integer | Unique mutual fund scheme code |
| date | Date | Date of NAV record |
| nav | Float | Net Asset Value of the fund |


## fact_transactions

| Column | Data Type | Description |
|---|---|---|
| investor_id | Text | Unique investor identifier |
| transaction_date | Date | Date of transaction |
| amfi_code | Integer | Mutual fund scheme code |
| transaction_type | Text | SIP, Lumpsum, or Redemption |
| amount_inr | Integer | Transaction amount in INR |
| state | Text | Investor state |
| city | Text | Investor city |
| kyc_status | Text | KYC verification status |


## fact_performance

| Column | Data Type | Description |
|---|---|---|
| amfi_code | Integer | Mutual fund scheme code |
| scheme_name | Text | Name of mutual fund scheme |
| fund_house | Text | AMC/Fund house name |
| category | Text | Fund category |
| return_1yr_pct | Float | 1 year return percentage |
| return_3yr_pct | Float | 3 year return percentage |
| return_5yr_pct | Float | 5 year return percentage |
| sharpe_ratio | Float | Risk adjusted return metric |
| sortino_ratio | Float | Downside risk adjusted return metric |
| beta | Float | Market sensitivity |
| expense_ratio_pct | Float | Fund expense ratio |
| risk_grade | Text | Risk classification |


## Source References

- NAV data: mfapi.in API
- Fund master and scheme data: AMFI mutual fund datasets
- Investor transaction data: Provided CSV dataset