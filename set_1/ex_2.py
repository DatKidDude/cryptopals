def bxor(text: bytes, key: bytes) -> bytes:
    """Cracks XOR cipher with text and key of same length"""

    if len(text) != len(key):
        raise ValueError("Strings must be of equal length")
    
    return bytes(x^y for (x, y) in zip(text, key))


hex_str = bytes.fromhex("1c0111001f010100061a024b53535009181c")
data = bytes.fromhex("686974207468652062756c6c277320657965")
expected_result = bytes.fromhex("746865206b696420646f6e277420706c6179")
result = bxor(hex_str, data)

assert result == expected_result, "Hex strings do not match"
