import requests


response = requests.get("https://www.usom.gov.tr/url-list.txt",verify=False)
file = open("usom.txt","w") # zararlı olan alan adları alınıp usom.txt dosyasına kaydedildi.
file.write(str(response.content))
file.close()