import pandas as pd


df = pd.read_csv("trgunlukrapor.csv")


#1- Gereksiz alanların silinmesi.
df.drop(["eriskin_yogun_bakim_doluluk_orani","eriskin_yogun_bakim_doluluk_orani","YBU","Ağır Hasta","yatak_doluluk_orani","ventilator_doluluk_orani"],axis=1,inplace=True)

#2- NaN olan bozuk verileri temizlenmesi
df.dropna(inplace = True)  

#3- Dosyada hakkındaki bilgiler.
result = df
result = df.columns
result = df.info

#4- ilk 5 kaydı gösterin
result = df.head()

#5- Son 5 kaydı gösterin
result = df.tail()
 
#6 Corona virüs türkiyede ilk hangi tarihte görülmüştür.
result = df[df["Günlük Vaka"] == df["Günlük Vaka"].min()]["Tarih"].iloc[0]

#7 2020-2021 tarihi arasında günlük vaka sayısının en fazla olduğu gün
result = df[df["Günlük Vaka"] == df["Günlük Vaka"].max()]["Tarih"].iloc[0]

#8 Toplam vefat sayısı
result = df["Toplam_Vefat"].sum() 

#9 Günlük Vefat sayısının en az oldugu tarih
result = df[df["Gunluk_Vefat"] == df["Gunluk_Vefat"].min()]["Tarih"].astype('datetime64[ns]').iloc[0]

#10 Günlük Vefat sayısının en fazla oldugu tarih
result = df[df["Gunluk_Vefat"] == df["Gunluk_Vefat"].max()]["Tarih"].astype('datetime64[ns]').iloc[0]

#11 2020-2021 yılları arasında ortalama hasta sayısı
result = df[["Gunluk_Hasta"]].mean().iloc[0]
 
print(result)