# My attempt at creating a base64 encoder and decoder.
# I plan on doing this again in the future and will implement bit shifting

import binascii
import string

def base64_encoder(source):
    """Encodes text to base64"""
    
    PADDING_CHAR = b"="
    B64_TABLE = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"

    # Convert source to binary string
    byte_string = "".join(format(char, "08b") for char in source).encode("ascii")

    # Pad bits to be a multiple of six
    padding_length = (6 - len(byte_string) % 6) % 6
    byte_string += b"0" * padding_length

    # Split byte string into 6 bit chunks
    chunks = [byte_string[i:i + 6] for i in range(0, len(byte_string), 6)]
    
    # Encode the text using the base64 table
    encoded_text = "".join(B64_TABLE[int(num, 2)] for num in chunks).encode("ascii")

    # Add padding chars
    encoded_text += PADDING_CHAR * (padding_length // 2)

    return encoded_text


def base64_decoder(source):
    """Decodes base64 encoded byte string"""

    # Base64 encoding table
    BASE64_TABLE = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"

    # Find the character index in b64 table
    b64_indices = [BASE64_TABLE.find(chr(char)) for char in source]

    # Convert characters back to 6 bits (Each padding bit converts to -1 or two "00")
    b64_string = b""
    for idx in b64_indices:
        if idx == -1:
            b64_string = b64_string[:-2]
        else:
            b64_string += format(idx, "06b").encode("ascii")

    # Get the original ascii byte values
    bytes_list = [b64_string[i:i + 8] for i in range(0, len(b64_string), 8)]
    
    # Decode to ascii value byte string
    decoded_text = bytes([int(chunk, 2) for chunk in bytes_list])

    return decoded_text

    
hex_string = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

expected_result = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

plaintext = b"Craig"

encoded_text = base64_encoder(plaintext)
decoded_text = base64_decoder(encoded_text)


# Verify encoding works
assert encoded_text == binascii.b2a_base64(plaintext, newline=False), "Encodings do not match"

# Verify decoding works
assert decoded_text == binascii.a2b_base64(encoded_text), "Decodings do not match"

