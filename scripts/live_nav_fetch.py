import requests
import pandas as pd
from pathlib import Path


schemes = {
    "HDFC_Top100": "125497",
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_LargeCap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}


save_path = Path("data/raw")


for name, code in schemes.items():

    print("\nFetching:", name)

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()


    nav_data = pd.DataFrame(data["data"])


    file_name = f"{name}_nav.csv"

    nav_data.to_csv(
        save_path / file_name,
        index=False
    )


    print("Saved:", file_name)


print("\nAll NAV files downloaded successfully")