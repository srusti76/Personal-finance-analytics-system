import pandas as pd
import numpy as np
df=pd.read_csv("PFA dataset\\Personal_Finance_Dataset.csv")
print(df)
print(df['Type'].unique())