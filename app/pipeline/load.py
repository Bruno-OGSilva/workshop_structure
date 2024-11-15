import os

import pandas as pd


def load_excel(
    data_frame: pd.DataFrame, output_path: str, file_name: str
) -> str:

    """
    receive a dataframe and save it as MS Excel

    args:
    data_frame (pd.DataFrame): dataframe to be saved as excel
    output_path (str): parth where the file will be saved
    file_name (str): file name to be saved

    return: "File saved successfuly".
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    data_frame.to_excel(f'{output_path}/{file_name}.xlsx', index=False)
    return 'File saved successfuly'
