import pandas as pd 

df = pd.read_csv("Churn_Modelling.csv")
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print("hello world")