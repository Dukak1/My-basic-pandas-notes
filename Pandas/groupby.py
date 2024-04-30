import pandas as pd
import numpy as np


personeller = {
    'çalışan':['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'departman':['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','Bilgi İşlem'],
    'yaş': [30,25,45,50,23,34,42],
    'semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Kadıköy','Tuzla','Maltepe'],
    'maaş': [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller)

result = df
result = df["maaş"].sum()

#groupby gruplar

result = df.groupby("departman").groups # Hangi departmanın kaç işçisi var
result = df.groupby(["departman","semt"]).groups # Herkesin departman ve semt bilgisi sonrada indisi


# for name,group in df.groupby("semt"):
#     print(name)
#     print(group)

# for name,group in df.groupby("departman"):
#     print(name)
#     print(group)

result = df.groupby("semt").get_group("Kadıköy") # sadece semti kadıköy olanları getirir

result = df.groupby("departman").get_group("Bilgi İşlem") # sadece bilgi işlemde çalışanları getirir

result = df.groupby("departman").sum() # departmana göre sınıflar ve değerleri toplar
# result = df.groupby("departman").mean() # departmana göre sınıflar ve değerlerin ortalamasını alır
result = df.groupby("departman")["maaş"].mean() # departmana göre sınıflar ve maaşların ortalamasını alır


result = df.groupby("semt")["yaş"].mean() # semte göre sınıflar ve yaşların ortalamasını alır
result = df.groupby("semt")["maaş"].mean() # semte göre sınıflar ve maaşların ortalamasını alır
result = df.groupby("semt")["çalışan"].count() # semte göre sınıflar ve hangi semtte kaç kişi yaşadığını sayar

result = df.groupby("departman")["yaş"].max() # departmana göre sınıflar ve departmandakiler arasından en büyüğünü getirir
result = df.groupby("departman")["maaş"].min() # departmana göre sınıflar ve departmandakiler arasından en düşük maaşı getirir

result = df.groupby("departman")["maaş"].max()["Muhasebe"] # muhasebeciler arasından maks maaş alanın maaşı



result = df.groupby("departman").agg(np.sum) # Bu niye çalışmıyor aq. sum çalışıyor ama mean

result = df.groupby("departman")["maaş"].agg([np.sum,np.max]) # strlerin ortalamasını alamıyor ama sum,max,min vs çalışıor

result = df.groupby("departman")["maaş"].agg([np.sum,np.max]).loc["Muhasebe"]
