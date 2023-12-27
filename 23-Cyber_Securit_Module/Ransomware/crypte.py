import os
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename='secret.key'):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def load_key(filename='secret.key'):
    return open(filename, 'rb').read()

def encrypt_file(key, filename):
    fernet = Fernet(key)

    with open(filename, 'rb') as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

def encrypt_folder(key, folder_path):
    fernet = Fernet(key)

    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)

            with open(file_path, 'rb') as file:
                file_data = file.read()

            encrypted_data = fernet.encrypt(file_data)

            with open(file_path, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)

# Anahtar oluşturma ve kaydetme
key = generate_key()
save_key(key)

# Klasör ve altındaki dosyaları şifreleme
folder_path = 'example_folder'
encrypt_folder(key, folder_path)
