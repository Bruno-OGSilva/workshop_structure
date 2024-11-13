import pandas as pd
from app.pipeline.transform import concatenate_dataframes

df_1 = pd.DataFrame({'col1': [1,2], 'col2': [3.4]})
df_2 = pd.DataFrame({'col1': [5,6], 'col2': [7.8]})

def test_concatenation_dataframe_list():
    arrange = pd.concat([df_1, df_2], ignore_index=True)

    act = concatenate_dataframes([df_1, df_2])

    assert arrange == act
