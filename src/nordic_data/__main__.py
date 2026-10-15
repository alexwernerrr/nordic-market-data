import datetime as dt
from nordic_data.riksbank import riksbank_data_fetch, json_to_df_parser


def main() -> None:
    
    # This is uselful so that todays date doesn't need to be manually hard coded
    todays_date = str(dt.date.today())
    date_one_month_ago = str(dt.date.today() - dt.timedelta(days=30))
    
    policy_rate_observation = riksbank_data_fetch("SECBREPOEFF", date_one_month_ago, todays_date)
    policy_rate_df = json_to_df_parser(policy_rate_observation)
    

if __name__ == "__main__":
    main()
