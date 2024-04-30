import pandas as pd

# s1 = pd.Series([3,2,0,1]) # başında indis değerleri yazan bir dizi oluşturduk
# s2 = pd.Series([0,3,7,2])

# data = dict(apples =s1, oranges = s2) # sözlük haline getirdik

# df = pd.DataFrame(data) # Dataframe yani 2 diziyi birleştirdik

# print(df)

#--------#

df = pd.DataFrame() # Yazdırırsak empty yani boş der
df = pd.DataFrame([1,2,3,4]) # Yazdırırsak indislerini belirterek 1,2,3,4 ten oluşan dizi verir. Satır indirsleri 0,1,2,3 Sütun indeksi sadece 0

df = pd.DataFrame([["Ahmet",50],["Ali",60],["Yağmur",70],["Çınar",80]]) #       0     1
                                                                        # 0  Ahmet   50 
                                                                        # 1     Ali  60
                                                                        # 2  Yağmur  70
                                                                        # 3   Çınar  80

data = [["Ahmet",50],["Ali",60],["Yağmur",70],["Çınar",80]]
df = pd.DataFrame(data,index = [1,2,3,4],columns = ['Name','Grade']) # Sütun adınları Name ve Grade yaptık. Satır indislerinide 0 dan değil 1 den başlattık. 

dict = {"Name": ["Ahmet","Ali","Yağmur","Çınar"],"Grade":[50,60,70,80]}
df = pd.DataFrame(dict)
df = pd.DataFrame(dict,index =["212","232","236","456"])

dict_list =[
                {"Name":"Ahmet","Grade":50},
                {"Name":"Ali","Grade":60},
                {"Name":"Yağmur","Grade":70},
                {"Name":"Çınar","Grade":0}
    ]

df = pd.DataFrame(dict_list)
df = pd.DataFrame(dict_list,index =["212","232","236","456"])

print(df)