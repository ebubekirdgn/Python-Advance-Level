
 # Ekrana hello ve gonderdigimiz isim degerini birlestirip yazan fonksiyon
def sayHello(name = 'user'):
    return 'Hello '+ name

msg = sayHello('Ebubekir')
msg = sayHello('Dogan')

print(msg)


#iki sayının toplamini veren fonksiyon
def total(num1, num2):
    return num1 + num2

result = total(10,20)
result = total(15,20)
print(result)




#Yas hesaplama fonksiyonu

def yasHesapla(dogumYili):
    return 2021 - dogumYili

ageDogan = yasHesapla(2017)
ageEbubekir = yasHesapla(2010)
ageMelih = yasHesapla(1999)

print(ageDogan, ageEbubekir, ageMelih)

def EmekliligeKacYilKaldi(dogumYili, isim):
    '''
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldı
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f'emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('Zaten emekli oldunuz')


EmekliligeKacYilKaldi(1983, 'Ali')
EmekliligeKacYilKaldi(1950, 'Ahmet')
EmekliligeKacYilKaldi(1974, 'Selim')

print(help(EmekliligeKacYilKaldi))

list = [1,2,3]

print(help(list.append))