import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data,index=['a','c','e','f','h'],columns =['column1','column2','column3'] )

df = df.reindex(['a','b','c','d','e','f','g','h']) # eksik olan b,d,g indislerinide ekledik ama buralarda şuan NaN yazıyor


result = df

result = df.drop('column1',axis=1) # column1 i siler. axis = 1 ise kolona, 0 ise satıra karşılık gelir
result = df.drop(['column1','column2'],axis=1) # column1 ve column2 yi siler. axis = 1 ise kolona, 0 ise satıra karşılık gelir

result = df.drop('a',axis=0) # a yı siler. axis = 1 ise kolona, 0 ise satıra karşılık gelir
result = df.drop(['a','b','c'],axis=0) # a b cyi siler. axis = 1 ise kolona, 0 ise satıra karşılık gelir

result = df.isnull() # NaN olanları True, değeri olanları False olarak gösterir
result = df.notnull() # NaN olanları False, değeri olanları True olarak gösterir

result = df.isnull().sum() # hangi kolonda kaç tane Null değer olduğunu toplar

result = df['column1'].isnull().sum() # column1 de kaç tane Null değer olduğunu toplar

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10] # yeni kolon oluşturup değerlerini verdik
df['column4'] = newColumn # oluşturduğumuz yeni kolonu df ye ekledik

result = df.dropna() # NaN (Null) değer olan satırları getirmez. axis = 0 dır yani

result = df.dropna(axis=1) # NaN (Null) değer olan sütunları getirmez. axis = 1 den dolayı sütun


result = df.dropna(how="any") # Her hangi bir satırda NaN varsa siler
result = df.dropna(how="all") # Tüm satır NaN ise siler


result = df.dropna(subset=['column1','column2']) # 1 ve 2. kolonda NaN varsa getirmez

result = df.dropna(subset=['column1','column2'],how="all") # 1 ve 2. kolonda NaN varsa getirmez

result = df.dropna(thresh=2) # NaN hariç 2 tane normal değer varsa silmez
result = df.dropna(thresh=3) # NaN hariç 3 tane normal değer varsa silmez


result = df.fillna(value="No input") # fillna, NaN ları doldurur. NaN değerlerin yerine No input yazar
result = df.fillna(value="1") # fillna, NaN ları doldurur. NaN değerlerin yerine 1 yazar


result = df.sum() # her kolonun toplam değerleri
result = df.sum().sum() # her kolonun toplam değerlerini toplar
result = df.size

result = df.isnull().sum()
result = df.isnull().sum().sum()


def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam/adet

result = df.fillna(value=ortalama(df)) # tüm null değerlere hesaplanan değer yazıldı

print(result)
# print(df)

