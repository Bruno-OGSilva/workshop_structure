import pandas as pd
from typing import List

"""
function to transform a dataframe list to a unique dataframe
"""

def concatenate_dataframes(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list, ignore_index=True)