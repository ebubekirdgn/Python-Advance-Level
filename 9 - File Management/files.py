# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w": (Write) yazma modu. 
#    ** Dosyayı konumda oluşturur. 
#    ** Dosya içeriğini siler ve yeniden ekleme yapar. 

# file = open("newfile.txt","w")
# file = open("C:/Users/Ebubekir Dogan/Desktop/deneme/newfile.txt","w")
# file.close()

file = open("newfile.txt","w",encoding='utf-8')
file.write("Ebubekir Dogan")
file.close()


# "w" : (Write) yazma modu.Dosyayı konumda oluşturur.
# "a" : (Append) ekleme.Dosya konumda yoksa oluşturur.
# "x" : (Create) oluşturma. Dosya zaten varsa hata verir.
# "r" : (Read) okuma. Varsayılan dosya konumda yoksa hata verir.



# "a": (Append) ekleme. Dosya konumda yoksa oluşturur. Verinin üzerine ekleme yapar
# file = open("newfile.txt","a",encoding='utf-8')
# file.write("\nEbubekir Dogan")
# file.write("Emir Asaf Dogan\n")
# file.close()

# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
# file = open("newfile2.txt","x",encoding='utf-8')

# "r": (Read) okuma. varsayılan. dosya konumda yoksa hata verir.
