import os
from cryptography.fernet import Fernet
from tkinter import filedialog
from tkinter import Tk, Button, Label

class FolderEncryptor:
    def __init__(self, master):
        self.master = master
        master.title("Klasör Şifreleme Uygulaması")

        self.label = Label(master, text="Klasör Seçimi:")
        self.label.pack()

        self.encrypt_button = Button(master, text="Klasörü Şifrele", command=self.encrypt)
        self.encrypt_button.pack()

        self.decrypt_button = Button(master, text="Klasör Şifresini Çöz", command=self.decrypt)
        self.decrypt_button.pack()

    def encrypt(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            key = generate_key()
            save_key(key)

            encrypt_folder(key, folder_path, delete_original=True)
            self.show_message(f"{folder_path} klasörü şifrelendi ve orijinal dosyalar silindi.")

    def decrypt(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            key = load_key()

            decrypt_folder(key, folder_path, delete_original=True)
            self.show_message(f"{folder_path} klasörünün şifresi çözüldü ve orijinal dosyalar silindi.")

    def show_message(self, message):
        self.label.config(text=message)

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename='secret.key'):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def load_key(filename='secret.key'):
    return open(filename, 'rb').read()

def encrypt_file(key, filename):
    fernet = Fernet(key)

    try:
        # Dosyayı aç ve okuma modunda kapat
        with open(filename, 'rb') as file:
            file_data = file.read()

        # Dosyanın adını değiştir ve tekrar yazma modunda aç, şifreleme işlemi uygula
        encrypted_filename = f"{filename}.encrypted"
        with open(encrypted_filename, 'wb') as encrypted_file:
            encrypted_file.write(fernet.encrypt(file_data))
    except Exception as e:
        print(f"Hata: {e}")

def decrypt_file(key, filename):
    fernet = Fernet(key)

    try:
        # Dosyanın adını değiştir ve tekrar yazma modunda aç, şifre çözme işlemi uygula
        decrypted_filename = filename.replace('.encrypted', '')
        with open(filename, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()

        with open(decrypted_filename, 'wb') as decrypted_file:
            decrypted_file.write(fernet.decrypt(encrypted_data))
    except Exception as e:
        print(f"Hata: {e}")

def encrypt_folder(key, folder_path, delete_original=False):
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            encrypt_file(key, file_path)

            if delete_original:
                os.remove(file_path)

def decrypt_folder(key, folder_path, delete_original=False):
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            decrypt_file(key, file_path)

            if delete_original:
                os.remove(file_path)

if __name__ == "__main__":
    root = Tk()
    app = FolderEncryptor(root)
    root.mainloop()
