import pandas as pd
import requests

# Save the url to api here for easier future use
BASE_URL = "https://api.riksbank.se/swea/v1/"


# The function is needed so that we work on the API-data with pandas
def json_to_df_parser(observations):
    
    df = pd.DataFrame(observations)
    
    # So that pandas-series aren't objects, which we can't handle
    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
    df["value"] = pd.to_numeric(df["value"])

    return df
    
# This function is used ot call the Riksbank API
def riksbank_data_fetch(series_id, start_date, end_date):
    
    # This is so that the user knows to enter dates as a string
    if not isinstance(start_date, str) or not isinstance(end_date, str):
        raise TypeError("Dates must be strings")
    
    # This is so it's clear whats the issue is if a user tries SECBREPOEFF/ for example
    if any("/" in s for s in (series_id, start_date, end_date)):
        raise ValueError("Inputs must not contain '/'")
    
    url = BASE_URL + "Observations" + "/" + series_id + "/" + start_date + "/" + end_date

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()


