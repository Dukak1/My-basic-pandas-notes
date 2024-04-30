import pandas as pd

data = pd.read_csv('yonelimfinal.csv')

data.dropna(inplace = True) # 'inplace = True' komutu güncellemek için kullanılır yani ;
                            # data = data.dropna() ile aynı şey


# data["Cinsiyet"] = data["Cinsiyet"].str.upper() # Cinsiyet kolonundakilerin bütün verilerini büyük harflerler yazar
# data["Cinsiyet"] = data["Cinsiyet"].str.lower() # Cinsiyet kolonundakilerin bütün verilerini küçük harflerler yazar

# data["index"] = data["Cinsiyet"].str.find('a') # index isimli yeni bir kolon ekler ve cinsiyet değerinde a harfi bulunup bulunmamasına göre 1 yada -1 döndürür

# data =data.Cinsiyet.str.contains('Erkek') # indislerden kadın olanları False erkek olanları True diye döndürür

# data =data[data.Cinsiyet.str.contains('Erkek')] # sadece cinsiyeti erkek olanları getirir


# data = data.parti.str.replace(' ','-') # parti kolonunda ki boşluklara - koyar

data[["Firstname",'Lastname']] = data['soru1'].loc[data['soru1'].str.split().str.len()==2].str.split(expand=True)


print(data.head(10))