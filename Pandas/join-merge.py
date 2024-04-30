import pandas as pd
"""
    customers ={
        'CustomerId':[1,2,3,4],
        'FirstName': ["Ahmet","Ali","Hasan","Canan"],
        'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
    }

    orders = {
        'OrderId':[10,11,12,13],
        'CustomerId':[1,2,5,7],
        'OrderData':["2010-07-04","2010-08-04","2010-07-07","2012-07-04"]
    }

    df_customers = pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
    df_orders = pd.DataFrame(orders,columns=["OrderId","CustomerId","OrderData"])

    print(df_customers)
    print(df_orders)

    result = pd.merge(df_customers,df_orders,how="inner") # kolonları yan yana birleştirir. Ama 3. ve 4. kayıtlar(customersda 3-4 ordersda 5-7) eşleşmediği için onlar yazılmaz vs sadece 2 satır getirilir
    result = pd.merge(df_customers,df_orders,how="left") # Soldakileri(df_customers) getir,sağdakileri(df_orders) getirme. Yani Bütün müşteriler (Siparişi olmayan müşterilerde) gelsin.Siparişi olmayanlar NaN getirir
    result = pd.merge(df_customers,df_orders,how="right") # Sağdakileri(df_order) getir,soldakileri(df_customers) getirme. Yani bütün siparişler gelir lakin siparişi olmayanlar için customers bilgileri Nan döndürür
    result = pd.merge(df_customers,df_orders,how="outer") # sağ-sol hep gelir
"""


customersA ={
    'CustomerId':[1,2,3,4],
    'FirstName': ["Ahmet","Ali","Hasan","Canan"],
    'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customersB ={
    'CustomerId':[4,5,6,7],
    'FirstName': ["Yağmur","Çınar","Cengiz","Can"],
    'LastName': ["Bilge","Turan","Yılmaz","Turan"]
}

df_customersA = pd.DataFrame(customersA,columns=["CustomerId","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB,columns=["CustomerId","FirstName","LastName"])

result = pd.concat([df_customersA,df_customersB]) # ilk data bilgileri yazılır, 2. data altına eklenir. axis = 0 olduğundan satıra göre işlem yapar.
result = pd.concat([df_customersA,df_customersB],axis=1) # ilk data bilgilerini yazar yanına 2.yi yazar. axis = 1 olduğundan sütuna göre işlem yapar.

print(result)

