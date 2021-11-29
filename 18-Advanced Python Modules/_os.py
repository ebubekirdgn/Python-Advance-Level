import os
import datetime

result = dir(os)
result = os.name

# dizin değiştirme
# os.chdir('C:\\')
# os.chdir('../..')

# klasör oluşturma
# os.mkdir("newdirectory")
# os.makedirs("newdirectory/yeniklasör")
# os.rename("newdirectory","yeniklasör")
# os.rmdir("newdirectory")
# os.removedirs("yeniklasör/yeniklasör")

# listeleme
# result = os.listdir()
# result = os.listdir('C:\\')
# for dosya in os.listdir():
#     if dosya.endswith('.py'): dosya uzantısının py ile bitip bitmedigi ile ilgili bilgi verir.
#         print(dosya)


# etkin dizin öğrenme
# result = os.getcwd()


# result = os.stat("_datetime.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime)  # oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime)  # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)  # değiştirilme tarihi

# os.system("notepad.exe")

# path

result = os.path.abspath("_os.py")
result = os.path.dirname("C:/python/advanced-modules/_os.py") 
result = os.path.dirname(os.path.abspath("_os.py")) # sadece dosya ismi bilinen dosyanın adresini bulma
result = os.path.exists("C:/python/advanced-modules/_os1.py") #dizin yada dosya ilgili konumda var mı yok mu 
result = os.path.exists("C:/python/advanced-modules") #dizin sorguladık.
result = os.path.isdir("C:/python/advanced-modules") #ulastıgımız alan klasor mu 
result = os.path.isfile("C:/python/advanced-modules/_os.py") # ulastıgımız alan dosya mı 
result = os.path.join("C:\\","deneme","deneme1")  #verdigimiz parcaları birlestiririz 
result = os.path.split("C:\\deneme") # dosya yolunu parcalar
result = os.path.splitext("_os.py") # dosya ismi ile uzantisini ayirir.
# result = result[0]
result = result[1]

print(result)