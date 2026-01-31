from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    raw_path=r"C:\Users\TRINADH PIDAPARTHI\OneDrive\Desktop\retail etl pipeline\data\raw\data.csv"
    output_path=r"C:\Users\TRINADH PIDAPARTHI\OneDrive\Desktop\retail etl pipeline\data\processed\clean_retail_data.parquet"

    df=extract_data(raw_path)
    df=transform_data(df)
    load_data(df,output_path)

    print(df.info())
run_pipeline()