from binascii import unhexlify, hexlify, b2a_hex, a2b_hex

def bxor(a, b):
    """bitwise XOR of bytestrings"""
    return bytes([x^y for (x, y) in zip(a,b)])


if __name__ == "__main__":
    hex_str = unhexlify(b"1c0111001f010100061a024b53535009181c")
    data = unhexlify(b"686974207468652062756c6c277320657965")
    expected_result = b"746865206b696420646f6e277420706c6179"

    result = bxor(hex_str, data)
    # print(result)
    # print("\n")
    # print(hexlify(result))
    # Remove 0x from result output
    assert hexlify(result) == expected_result, "Hex strings do not match"
