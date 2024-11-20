import binascii
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

# Key and file details
key = b"YELLOW SUBMARINE"  # 16-byte key for AES-128
input_file = "data7.txt"

# Read the Base64-encoded content
with open(input_file, "rb") as file:
    # Decode the Base64-encoded content
    base64_content = binascii.a2b_base64(file.read())
 
# Decrypt the ciphertext using AES-128-ECB
cipher = AES.new(key, AES.MODE_ECB)
decrypted = cipher.decrypt(base64_content)


try:
    plaintext = unpad(decrypted, AES.block_size)
except ValueError:
    print("Error: Padding is invalid or not present")
    plaintext = decrypted

print(plaintext.decode("utf-8"))
