from pipeline.extract import extract_from_excel
from pipeline.transform import concatenate_dataframes
from pipeline.load import load_excel


if __name__ =="__main__":
    dataframe_lists = extract_from_excel("data/input")
    data_frame = concatenate_dataframes(dataframe_lists)
    load_excel(data_frame, "data/output", "output")