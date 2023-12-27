import os
from cryptography.fernet import Fernet

def load_key(filename='secret.key'):
    return open(filename, 'rb').read()

def decrypt_file(key, filename):
    fernet = Fernet(key)

    with open(filename, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(filename, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

def decrypt_folder(key, folder_path):
    fernet = Fernet(key)

    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)

            with open(file_path, 'rb') as encrypted_file:
                encrypted_data = encrypted_file.read()

            decrypted_data = fernet.decrypt(encrypted_data)

            with open(file_path, 'wb') as decrypted_file:
                decrypted_file.write(decrypted_data)

# Anahtarı yükleme
key = load_key()

# Klasör ve altındaki dosyaları çözme
folder_path = 'C:/Users/DoganPc/Desktop/ransomware/deneme/'
decrypt_folder(key, folder_path)
