import pandas as pd
import numpy as np

data = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,20,25],
    "Column3": ["abc","bcaa","ade","cb","dea"]
}

df = pd.DataFrame(data)

def kareal(x):
    return x * x

kareal2 = lambda x: x * x

result = df
result = df["Column2"].unique() #tekrarlamayan bilgileri verir.
result = df["Column2"].nunique() #tekrarlanmayan elemanların sayısını verir.
result = df["Column2"].value_counts() # her bir elemanın kaç defa tekrarladıgını verir.
result = df["Column1"] * 2 
result = df["Column1"].apply(kareal) #column1 icindeki degerler sırasıyla kareal methoduna verilir.
result = df["Column1"].apply(kareal2) # yukarıdaki ile aynı işi yapar.
result = df["Column1"].apply(lambda x: x * x) 
df["Column4"] = df["Column3"].apply(len) #Column3 icindeki her elemanın kaç karakter oldugunu verir.

result = df.columns 
result = len(df.columns) # column adetini verir.
result = df.index # kac adet oldugunu ve kacar kacar arttıgını verir.
result = len(df.index) # 5 satir oldugunu verir.
result = df.info

result = df.sort_values("Column2")  # Column2 ye göre sıralama yapar.
result = df.sort_values("Column3")  # Column3 ye göre sıralama yapar.
result = df.sort_values("Column3", ascending = False)  # Column3 ye göre sıralama yapar ancak azdan coga dogru artırır.

data = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data)

print(df.pivot_table(index="Ay",columns= "Kategori", values= "Gelir"))