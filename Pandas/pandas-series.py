import pandas as pd
import numpy as np

# data

numbers= [20,30,40,50]
letters = ['a','b','c',20]
scalar = 5
dict = {'a':10,'b':20,'c':30,'d':40}
random_numbers = np.random.randint(10,100,6)

pandas_series = pd.Series()
pandas_series = pd.Series(numbers)
pandas_series = pd.Series(letters) # pandas da her veri aynı veri tipinde olmak zorunda değil. Hem int hem str varsa object olarak döndürür.
pandas_series = pd.Series(scalar,[0,1,2,3]) # 5 i 4 kere yazdırır
pandas_series = pd.Series(numbers,['a','b','c','d']) # abcd burda key bilgileri. normalde 0123 olur
pandas_series = pd.Series(dict)
pandas_series = pd.Series(random_numbers)
# print(pandas_series)


pandas_series = pd.Series([20,30,40,50],['a','b','c','d'])

result = pandas_series[0]
result = pandas_series[-1]
result = pandas_series[:2] # ilk 2 eleman
result = pandas_series[-2:] # son 2 eleman
result = pandas_series['a'] # a keyine denk gelen value
result = pandas_series[['a','c']] 
# result = pandas_series[['a','c','e']] # e ye karşılık NaN döndürür (not a number). Ama bende hata döndürüyor aq
result = pandas_series.ndim # 1 boyutlu
result = pandas_series.dtype # data type yani int,str,float gibi bişey
result = pandas_series.shape # şekli
result = pandas_series.sum() # topla 140
result = pandas_series.max() # maksı bulur
result = pandas_series.min() # mini bulur

result = pandas_series + pandas_series # Value lar 2x olur
result = pandas_series + 50 # Value lar + 50 olur

result = np.sqrt(pandas_series) # karakök
result = pandas_series >= 50 # Boolen döndürür
result = pandas_series %2 == 0 # Boolen döndürür

# print(pandas_series)
# print(result)

#-------#

opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([40,30,20,10],["astra","corsa","grandland","insignia"])

total = opel2018 + opel2019

print(total)
# print(total["astra"])
# print(total["combo"]) # hata çevirir