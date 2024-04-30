import pandas as pd
from numpy.random import randn


df = pd.DataFrame(randn(3,3),index = ["A","B","C"],columns = ["Column1","Column2","Column3"])

result = df
result = df["Column1"]
result = type(df["Column1"])
result = df[["Column1","Column2"]]

# loc["row","column"] => loc ["row"] => loc[":","column"]
result = df.loc["A"] # A sütununun adını (A) ve veri tipini getirir  # Çokomelli
result = type(df.loc["A"]) 
result = df.loc[:,"Column1"] # Sadece column1 i yazdırır ve column1 in ismini(Column1) ve veri tipini getirir
result = df.loc[:,["Column1","Column2"]] # Column1 ve Column2 yi yazdırır

result = df.loc[:,"Column1":"Column3"] # Column1 den Column3 e kadar yazdırır. (Column3 dahil)
result = df.loc[:,:"Column3"] # Column1 den Column3 e kadar yazdırır. (Column3 dahil)
result = df.loc["A":"B",:"Column3"] # Sadece A ve B satırlarını getirir. C yi getirmez
result = df.loc[:"B",:"Column3"] # Sadece A ve B satırlarını getirir. C yi getirmez

result = df.iloc[2] # 2. indisin (C) adını ve veri tipini getirir # Çokomel

result = df.loc["A","Column2"] # Sadece A satırının 2. kolonunu getirir
result = df.loc["C","Column3"] # Sadece C satırının 3. kolonunu getirir
result = df.loc[["A","B"],"Column1"] # A ve B satırlarının 1. kolonunu getirir
result = df.loc[["A","B"],["Column1","Column2"]] # A ve B satırlarının 1. ve 2. kolonunu getirir

df["Column4"] = pd.Series(randn(3),["A","B","C"]) # 4. kolonu ekler
df["Column5"] = df["Column1"] + df["Column3"] # 1 ve 3. kolonun değerlerini toplayıp 5. kolonu oluşturur.

result = df.drop("Column5",axis=1,inplace = True) # 5. kolonu siler. inplace = True kısmını videodan izle anlamadım

print(df)

print(result)