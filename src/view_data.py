import pandas as pd

def view_and_convert_data():
    # Load the parquet file
    df = pd.read_parquet(r"C:\Users\TRINADH PIDAPARTHI\OneDrive\Desktop\retail etl pipeline\data\processed\clean_retail_data.parquet")

    # Save as CSV for readability
    csv_path = r"C:\Users\TRINADH PIDAPARTHI\OneDrive\Desktop\retail etl pipeline\data\processed\clean_retail_data.csv"
    df.to_csv(csv_path, index=False)
    print(f"✓ CSV file saved to: {csv_path}")

    # Display summary
    print(f"\nDataset Info:")
    print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"\nColumns: {df.columns.tolist()}")
    print(f"\nFirst 10 rows:")
    print(df.head(10).to_string())
    print(f"\nData types:")
    print(df.dtypes)

# Run when called directly
if __name__ == "__main__":
    view_and_convert_data()
