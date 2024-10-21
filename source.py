from hashlib import sha256
import string, random
from secret import MASTER_KEY, FLAG
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode

ALPHABET = string.ascii_letters + string.digits + '~!@#$%^&*'

def crack_masterKey(password):
    return sum(1 << i for i, p in enumerate(password) if p in ALPHABET[:len(ALPHABET) // 2]).to_bytes((7 + len(password)) // 8, 'little')

   

def generate_password():
    master_key = int.from_bytes(MASTER_KEY, 'little')
    password = ''

    while master_key:
        bit = master_key & 1
        if bit:
            password += random.choice(ALPHABET[:len(ALPHABET)//2])
        else:
            password += random.choice(ALPHABET[len(ALPHABET)//2:])
        master_key >>= 1

    return password


def main():
    password = 't*!zGnf#LKO~drVQc@n%oFFZyvhvGZq8zbfXKvE1#*R%uh*$M6c$zrxWedrAENFJB7xz0ps4zh94EwZOnVT9&h'
    ciphertext = 'GKLlVVw9uz/QzqKiBPAvdLA+QyRqyctsPJ/tx8Ac2hIUl8/kJaEvHthHUuwFDRCs'
    
    master_key = crack_masterKey(password)
    encryption_key = sha256(master_key).digest()
    cipher = AES.new(encryption_key, AES.MODE_ECB)

    print("Decrypted MASTER_KEY: " + master_key.decode())
    print("Flag: " + unpad(cipher.decrypt(b64decode(ciphertext)), AES.block_size).decode())

if __name__ == '__main__':
    main()


