def load_data(df,output_path:str)->None:
    df.to_parquet(output_path, index=False)