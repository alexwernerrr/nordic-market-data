from pathlib import Path
import pandas as pd
import json
from nordic_data.riksbank import json_to_df_parser
from nordic_data.paths import PROJECT_ROOT

# This is defines here for easier access to the test data
TEST_DATA_DIR = Path(PROJECT_ROOT / "tests" / "data")


# This test is to make sure the json_to_df_parser hasn't broken 
def test_json_to_df_parser():
    
    with open(TEST_DATA_DIR / "riksbank_policy_rate.json", "r") as f:
        riksbank_sample_policy_rate = json.load(f)
    
    policy_rate_df = json_to_df_parser(riksbank_sample_policy_rate)

    assert len(policy_rate_df) == 23
    assert list(policy_rate_df.columns) == ["date", "value"]
    assert policy_rate_df["date"].iloc[0] == pd.Timestamp("2026-09-01")
    assert policy_rate_df["value"].iloc[0] == 1.75

