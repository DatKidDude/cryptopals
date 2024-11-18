import binascii

# Initialize string
hex_string = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

solution = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

b64_encoding = binascii.b2a_base64(binascii.unhexlify(hex_string), newline=False)

assert b64_encoding == solution, "Encodings do not match"