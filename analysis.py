import pandas as pd
import numpy as np
df=pd.read_csv("PFA dataset\\Personal_Finance_Dataset.csv")
print(df)
print(df['Type'].unique())
#selecting particular column and check paritcular value 
print(df[df['Type']=='Income'])
#checking shape (rows*columns)
print(df.shape)
#checking null values (missing values)
print(df.isnull())
#checking duplicate values
print(df.duplicated())
print(df.duplicated().sum())
print(df.dtypes)
print(df['Date'].dtypes)

#converting date column(which was str type) into date time format
df['Date']=pd.to_datetime(df['Date'],format='%d-%m-%Y')
print(df['Date'])
print(df['Date'].dtypes)
print(df['Date'].min())
print(df['Date'].max())
SumofIncome=df[df['Type']=='Income']['Amount'].sum()
print(SumofIncome)
SumofExpenses=df[df['Type']=='Expense']['Amount'].sum()
print(SumofExpenses)
Net_Balance=SumofIncome-SumofExpenses
print(Net_Balance)
expensesbycategory=df[[df['Type']['Category']['Amount']]].groupby()
print(expensesbycategory)