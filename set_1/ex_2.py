from binascii import unhexlify, hexlify
from crypto_utils import fixed_size_xor

hex_str = unhexlify(b"1c0111001f010100061a024b53535009181c")
data = unhexlify(b"686974207468652062756c6c277320657965")
expected_result = b"746865206b696420646f6e277420706c6179"

result = fixed_size_xor(hex_str, data)

assert hexlify(result) == expected_result, "Hex strings do not match"
