from binascii import unhexlify, hexlify

def bxor(a, b):
    """bitwise XOR of bytestrings"""
    return hex(int(a, 16) ^ int(b, 16))
    # return bytes([x^y for (x, y) in zip(a,b)])

hex_str = "1c0111001f010100061a024b53535009181c"
data = "686974207468652062756c6c277320657965"
expected_result = "746865206b696420646f6e277420706c6179"

result = bxor(hex_str, data)
print(result[2:])
print(type(result))

# Remove 0x from result output
assert result[2:] == expected_result, "Hex strings do not match"
