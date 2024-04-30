import pandas as pd
import numpy as np

data = {
    "Column1":[1,2,3,4,5],
    "Column2":[10,20,13,45,25],
    "Column3":["abc","bcaa","ade","cb","dea"]
}

df = pd.DataFrame(data)

def kareal1(x):
    return x*x

kareal2=lambda x:x*x

result = df
result = df["Column2"].unique() # kolon 2 deki tekrarlanmayan değerleri getirir
result = df["Column2"].nunique() # kolon 2 de tekrarlanmayan kaç sayı olduğunu döndürür

result = df["Column2"].value_counts() # kolon 2 de her sayıdan kaç tane olduğunu döndürür

result = df["Column1"].apply(kareal1) # apply methodu fonksiyon çalıştırmaya yarar. Bunun sayesinde kolon 1 değerlerinin karesini alırız. Column1 deki değerler tek tek kareal1(x) de ki x yerine koyulur
result = df["Column1"].apply(kareal2) # lambda fonksiyonlarda çalışır.
result = df["Column1"].apply(lambda x:x*x) # Bu da çalışır.31

result = df["Column3"].apply(len) # kolon 3 deki her verinin karakter uzunluğunu belirtir. abc 3 bcaa 4 gibi

"""
df["Column4"]= df["Column3"].apply(len) # kolon3 ün veri uzunluklarını belirten Column4 ü ekleriz
print(df)
"""
result = df.columns # kolonların adlarını ve dtype değerini döndürür
result = len(df.columns) # kaç kolon olduğunu döndürür 
result = df.index # index bilgileri
result = len(df.index) # index bilgilerinin uzunluğu. Burada 5 misal
result = df.info # kolon satır bilgileri vsvs


result = df.sort_values("Column2") # Kolon 2 ye göre sıralar. küçükten büyüğe
result = df.sort_values("Column2",ascending=False) # Büyükten küçüğe
result = df.sort_values("Column3") # Kolon 3 e göre sıralar. A'dan Z'ye
result = df.sort_values("Column3",ascending=False) # Buda Z'den A'ya

# print(result)


data2={
    "Ay":["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori":["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir":[20,30,15,14,32,52,12,36,52]

}

df =pd.DataFrame(data2)
df = df.pivot_table(index="Ay",columns="Kategori",values="Gelir") # Satırlar Ay, kolonlar kategori,değerler gelirden gelir. İyimiş he




print(df)