from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

KEY = b"YELLOW SUBMARINE"

if __name__ == "__main__":  
    with open("challenge7_input.txt", "r") as f:
        ciphertext = base64.b64decode(f.read())

    cipher = AES.new(KEY, AES.MODE_ECB)
    plaintext_padded = cipher.decrypt(ciphertext)
    print(plaintext_padded.decode("utf-8"))
