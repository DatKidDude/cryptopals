# Repeating XOR Cipher
from binascii import hexlify
import codecs

def repeating_key_xor(text: bytes, key: bytes) -> bytes:
    """Encrypt text using a repeated XOR cipher"""

    result = []
    for i in range(len(text)):
        j = i % len(key)

        result.append(chr(text[i] ^ key[j]))


    hexx = "".join(result).encode("ascii")

    encoded_text = codecs.encode(hexx, "hex")

    return encoded_text

# Line break character needed to match the solution 
text = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

solution = b"0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    
key = b"ICE"

encoded_text = repeating_key_xor(text, key)

# Verify my solution
assert encoded_text == solution, "Not equal"

