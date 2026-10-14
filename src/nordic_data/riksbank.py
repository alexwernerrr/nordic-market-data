import pandas as pd
import json


# The function is needed so that we work on the API-data with pandas
def json_to_df_parser(json):
    
    df = pd.DataFrame(json)
    
    # So that pandas-series aren't objects, which we can't handle
    df["date"] = pd.to_datetime(df["date"], format="mixed")
    df["value"] = pd.to_numeric(df["value"], errors="coerce")

    return df
    

