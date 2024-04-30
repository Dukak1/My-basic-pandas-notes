import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)

df = pd.DataFrame(data,columns = ["column1","column2","column3","column4","column5"])

result = df
result = df.columns # kolonların bilgilerini getirir.

result= df.head() # İlk 5 satırı getirir.
result= df.head(10) # İlk 10 satırı getirir.
result= df.tail() # Son 5 satırı getirir.
result= df.tail(10) # Son 10 satırı getirir.

result = df["column1"].head() # 1. kolonun ilk 5 değeri, kolonun adı ve veri tipi
result = df.column1.head() # 1. kolonun ilk 5 değeri, kolonun adı ve veri tipi

result = df[["column1","column2"]].head() # 1 ve 2. kolonların ilk 5 değeri
result = df[["column1","column2"]].tail() # 1 ve 2. kolonların son 5 değeri


result = df[5:15][["column1","column2"]] # 5 15 arası 1 ve 2. kolon değerleri
result = df[5:15][["column1","column2"]].head() # 5 15 arası ilk 5 değer(5,6,7,8,9) 1 ve 2. kolon değerleri
result = df[5:15][["column1","column2"]].tail() # 5 15 arası son 5 değer(10,11,12,13,14) 1 ve 2. kolon değerleri

result = df >50 # 50 den büyük yada küçük olmasına göre True False döndürür
result = df[df>50] # 50 den küçükler için NaN yani not a number döndürür
result = df[df%2==0] # tek sayılar için NaN döndürür

result = df["column1"] > 50 # 1. kolondakilere göre True False
result = df[df["column1"] >50] # 1. kolondaki sadece 50 den büyük değerleri getirir. Bune mq

result = df[(df["column2"] >50) & (df["column2"] <= 70)] # 2. kolonun 50 den büyük VE 70den küçük eşit olanları getirir
result = df[(df["column2"] >50) | (df["column2"] <= 70)] # 2. kolonun 50 den büyük VEYA 70den küçük eşit olanları getirir vay aq

# query

result = df.query("column1 >=50 & column1 %2 == 0" ) # 1. kolonda 50'ye eşit büyük VE çift sayıları getirir
result = df.query("column1 >=50 & column1 %2 == 0" )[["column1","column2"]] # 1.ve 2. kolonda 50'ye eşit büyük VE çift sayıları getirir
result = df.query("column1 >=50 | column1 %2 == 0" )[["column1","column2"]] # 1.ve 2. kolonda 50'ye eşit büyük VEYA çift sayıları getirir


print(result)

