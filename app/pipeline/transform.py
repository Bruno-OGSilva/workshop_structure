from typing import List

import pandas as pd




def concatenate_dataframes(
    data_frame_list: List[pd.DataFrame],
) -> pd.DataFrame:
    """
    function to transform a dataframe list to a unique dataframe.
    """
    return pd.concat(data_frame_list, ignore_index=True)
