from cryptography.fernet import Fernet

file = open('key', 'rb')
key = file.read()
file.close()

# open the file to encrypt
with open('test.encrypted', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

# write the encrypted file
with open('test.decrypted', 'wb') as f:
    f.write (encrypted)


