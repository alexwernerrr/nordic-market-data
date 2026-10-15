import pandas as pd



# The function is needed so that we work on the API-data with pandas
def json_to_df_parser(observations):
    
    df = pd.DataFrame(observation)
    
    # So that pandas-series aren't objects, which we can't handle
    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
    df["value"] = pd.to_numeric(df["value"])

    return df
    

