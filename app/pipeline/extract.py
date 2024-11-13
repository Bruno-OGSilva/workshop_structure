import os 
import glob

import pandas as pd

from typing import List

"""
function to read the files from a folder data/input and return a dataframe list

args: input_path (str): folder path with the files

return: dataframe list
"""
#path = "data/input"

def extract_from_excel(path: str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(path, "*.xlsx"))
    
    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))
    return data_frame_list

if __name__ == "__main__":
    data_frame_list = extract_from_excel(path= "data/input")
    print(data_frame_list)