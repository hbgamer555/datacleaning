import csv
import pandas as pd

df=pd.read_csv("dwarfstars.csv")
print(df.shape)
print(df.head())
del df["Luminosity"]
print(df.shape)