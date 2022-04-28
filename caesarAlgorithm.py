# Caesar Encryption
def encryption(text, key):
    encrypted_text = ""
    for i in range(len(text)):
        if text[i] == ' ':
            encrypted_text += " "
        elif (text[i].isupper()):
            encrypted_text += chr((ord(text[i]) + key - 65) % 26 + 65)
        else:
            encrypted_text += chr((ord(text[i]) + key - 97) % 26 + 97)
    return encrypted_text

def decryption(text, key):
    decrypted_text = ""
    for i in range(len(text)):
        if text[i] == ' ':
            decrypted_text += " "
        elif (text[i].isupper()):
            decrypted_text += chr((ord(text[i]) - key - 65) % 26 + 65)
        else:
            decrypted_text += chr((ord(text[i]) - key - 97) % 26 + 97)
    return decrypted_text

text = input("Enter text: ")
key = int(input("Enter key: "))

print("Encrypted text: " + encryption(text, key))

decryption_key = int(input("enter key to decrypt your text: "));
print(decryption(encryption(text, key), decryption_key))
