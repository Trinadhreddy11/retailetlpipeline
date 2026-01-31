import pandas as pd
def transform_data(df:pd.DataFrame)->pd.DataFrame:
   df.columns=df.columns.str.lower().str.replace(' ','_').str.strip()
   df['invoicedate']=pd.to_datetime(df['invoicedate'])

   #elinate useless data
   df=df.dropna(subset=['invoiceno','description'])
   df=df[(df['quantity']>0) & (df['unitprice']>0)]

   #standardize text data
   df['country']=df['country'].str.lower().str.strip().str.title()
   df['description']=df['description'].str.lower().str.replace(r'[^A-Za-z0-9]','',regex=True)

   #type casting
   df['invoiceno']=pd.to_numeric(df['invoiceno'], errors='coerce')
   df['customerid']=pd.to_numeric(df['customerid'], errors='coerce')

   #additional features
   df['revenue']=df['quantity']*df['unitprice']
   df['year']=df['invoicedate'].dt.year
   
   #remove outliers
   df=df[(df['quantity']<10000) & (df['unitprice']<10000)]
   return df