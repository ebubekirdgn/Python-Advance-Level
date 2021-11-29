import pandas as pd


customers = {
    'CustomerId' : [1,2,3,4],
    'FirstName'  : ["Ebubekir","kerim","Selim","Ahmet"],
    'LastName'  : ["Doğan","Menekşe","Saraç","Sara"]
} 

orders = {
    'OrderId' : [10,20,30,40],
    'CustomerId'  : [1,2,5,7],
    'OrderDate'  : ['2022-10-12','2021-11-12','2019-10-12','2022-10-13']
} 

df_customers = pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
df_orders = pd.DataFrame(orders,columns=["OrderId","CustomerId","OrderDate"])

#print(df_customers)
#print(df_orders)

result = pd.merge(df_customers,df_orders,how="inner") #siparisi ve musteri bilgisi varsa 
result = pd.merge(df_customers,df_orders,how="left") # musteri bilgisi var siparisi yoksa 
result = pd.merge(df_customers,df_orders,how="right") # siparis var ancak musteri bilgisi yoksa bunu kullanırız
result = pd.merge(df_customers,df_orders,how="outer") # tamamını getirir


customersA = {
    'CustomerId': [1,2,3,4],
    'FirstName': ["Ahmet","Ali","Hasan","Canan"],
    'LastName': ["Yılmaz","Korkmaz","Çelik","Çamur"]
}

customersB = {
    'CustomerId': [4,5,6,7],
    'FirstName': ["Ayşe","Selim","Melike","Fatma"],
    'LastName': ["Yılmaz","Yaprak","Yılmaz","Turan"]
}
df_customersA = pd.DataFrame(customersA, columns = ["CustomerId","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB, columns = ["CustomerId","FirstName","LastName"])

result = pd.concat([df_customersA,df_customersB])
result = pd.concat([df_customersA,df_customersB],axis=1) #birleştirme işlemi yapıyoruz.

print(result)