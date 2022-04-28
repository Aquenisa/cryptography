
Vernam Encryption
import random
import string

def encryption(text, key):
    encrypted_text = ""
    for i in range(len(text)):
        if text[i] == ' ':
            encrypted_text += " "
        elif (text[i].isupper()):
            encrypted_text += chr(((ord(text[i]) + (ord(key[i%len(key)]) - 65)) - 65) % 26 + 65)
        else:
            encrypted_text += chr((ord(text[i]) + (ord(key[i%len(key)]) - 65) - 97) % 26 + 97)
    return encrypted_text

def decryption(text, key):
    decrypted_text = ""
    for i in range(len(text)):
        if text[i] == ' ':
            decrypted_text += " "
        elif (text[i].isupper()):
            decrypted_text += chr(((ord(text[i]) - (ord(key[i%len(key)]) - 65)) - 65) % 26 + 65)
        else:
            decrypted_text += chr((ord(text[i]) - (ord(key[i%len(key)]) - 65) - 97) % 26 + 97)
    return decrypted_text


text = input("Enter text: ")
key = ""
for i in range(len(text)):
    key += random.choice(string.ascii_lowercase)

print("Your key is: ", key)
print("Encrypted text: " + encryption(text, key))

decryption_key = input("enter key to decrypt your text: ")
print(decryption(encryption(text, key), decryption_key))
