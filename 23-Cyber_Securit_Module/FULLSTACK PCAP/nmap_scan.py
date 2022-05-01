# Bilgisayarınızda nmap kurulu olmalıdır
# Python kütüphanesini kurmak için
# pip install python-nmap


import nmap

basla = 75 # taramanın başlatılacağı port
bitis = 80 # taramanın bitirileceği port

hedef = '192.168.1.1' # Hedef ip

scanner = nmap.PortScanner()

for i in range(basla, bitis+1):
    res = scanner.scan(hedef, str(i))
    res = res['scan'][hedef]['tcp'][i]['state']
    print(f'port {i} - {res}')

