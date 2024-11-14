import codecs
import binascii, base64

# Initiale string
hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

b64 = codecs.encode(codecs.decode(hex_string, "hex"), "base64")
print(b64)

# b64_string = base64.b64encode(binascii.unhexlify(hex_string))
# print(b64_string)