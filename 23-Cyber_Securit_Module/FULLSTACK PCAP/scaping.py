# BeautifulSoup kütüphanesini kurmak için
# pip install bs4

from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen

site = 'https://www' # hedef web sitesi

# karşı tarafa kendimizi web tarayıcısı gibi göstermek için
# başlık ekliyoruz
baslik = {'User-Agent':'Mozilla/5.0'}

# bağlantı talebimizi oluşturuyoruz
req = Request(site, headers=baslik)

# web sayfasına bağlanıyoruz ve kaynak kodu alıyoruz
page = urlopen(req)

# page değişkenine aldığımız kaynak kodları html olarak parçalıyoruz
soup = bs(page,'html.parser' )

# kaynak kod içerisindeki a komutlarından class değeri card-link
# olanları seçiyoruz
link = soup.findAll('a', class_='card-link')
for i in link:
    print(i['title'])