  #!/usr/bin/python3
import os
from time import sleep
import pyshorteners

os.system('clear')

def Main():
    print("\n[*1]  Google")
    print("[*2]  Youtube")
    print("[*3]  Spotify")
    print("[*4]  Instagram")
    print("[*5]  Facebook")
    print("[*6]  New York Times")
    print("[*7]  CTF")
    print("\n[*99]  Exit")
    Selector()


def Selector():
    select = int(input("\nBirini Secin: "))
    if select == 1:
        EnlaceGoogle()
    elif select == 2:
        EnlaceYoutube()
    elif select == 3:
        EnlaceSpotify()
    elif select == 4:
        EnlaceInstagram()
    elif select == 5:
        EnlaceFacebook()
    elif select == 6:
        EnlaceNewyorkTimes()
    elif select == 7:
        EnlaceCTF()
    elif select == 99:
        os.system('clear')
        print("Goodbye...")
        sleep(1)
        os.system('clear')
        exit()
    else:
        os.system('clear')
        print("Dogru bir secim degil")
        sleep(1)
        os.system('clear')
        Main()


def EnlaceGoogle():
    os.system('clear')
    print("Google Seçildi.")
    OriginalLink = str(input("\nOrijinal URL: "))
    
    Postlink = str(input("\nPost LINK: "))
    os.system('clear')
    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    print(f"\033[95m\nGizli Link: https://www.google.com-{Postlink}@{Withouthttp}")
    
    Other()

def EnlaceYoutube():
    os.system('clear')
    print("Youtube Seçildi.")
    OriginalLink = str(input("\nOrijinal URL: "))
    
    Postlink = str(input("\nPost LINK: "))
    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    os.system('clear')
    print(f"\033[95m\nGizli Link: https://www.youtube.com-video-{Postlink}@{Withouthttp}")
    
    Other()

def EnlaceSpotify():
    os.system('clear')
    print("Spotify Seçildi.")
    OriginalLink = str(input("\nOrijinal URL: "))
    
    Postlink = str(input("\nPost LINK: "))
    Shortener = pyshorteners.Shortener()
    H=a29udWxhci8=
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    os.system('clear')
    print(f"\033[95m\nGizli Link: https://www.spotify.com-video-{Postlink}@{Withouthttp}")
    
    Other()

def EnlaceInstagram():
    os.system('clear')
    print("Instagram Seçildi.")
    OriginalLink = str(input("\nOrijinal URL: "))
    
    Postlink = str(input("\nPost LINK: "))
    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    os.system('clear')
    T=aW50ZXJuYXRpb25hbC10ZWFtLWFsaW1sYXJpLWFjaWxtaXN0aXI=
    print(f"\033[95m\nGizli Link: https://www.instagram.com-photo-{Postlink}@{Withouthttp}")
    
    Other()

def EnlaceFacebook():
    os.system('clear')
    print("Facebook Seçildi.")
    OriginalLink = str(input("\nOrijinal URL: "))
    
    Postlink = str(input("\nPost LINK: "))
    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    os.system('clear')
    print(f"\033[95m\nGizli Link: https://www.facebook.com-profile-{Postlink}@{Withouthttp}")
    Other()

def EnlaceNewyorkTimes():
    os.system('clear')
    print("New York Times Seçildi.")
    OriginalLink = str(input("\nOriginal URL: "))
    
    Postlink = str(input("\nPost LINK: "))
    Shortener = Pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    os.system('clear')
    print(f"\033[95m\nGizli Link: https://www.newyorktimes.com-{Postlink}@{Withouthttp}")
    
    Other()

def EnlaceCTF():
    os.system('clear')
    print("Yanlış yeri seçtin")
    Domain = str(input("ERROR"))
    OriginalLink = str(input("\nERROR: "))
    
    print("\nERROR")
    Postlink = str(input("\nPost LINK: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    os.system('clear')
    
    Other()

def Other():
    print("\033[93m\nBaşka linklere göz atmak ister misiniz?")
    print("Evet [*1] \nHayır  [*2]")
    IT=LjE5NjYwNzcv
    select=int(input("\nBirini seçin: "))
    if select == 1:
        os.system('clear')
        Main()
    else:
        os.system('clear')
        exit()

#SYSCALL

Main()

input()
