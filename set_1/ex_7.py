import binascii

with open("data7.txt", "rb") as f:
    data = binascii.a2b_base64(f.read())

    print(binascii.hexlify(data))
