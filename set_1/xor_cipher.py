# Single byte xor cipher implementation

def single_byte_xor(text: bytes, key: int) -> bytes:
    """Given a plain text 'text' as bytes and an encryption key 'key' as a byte in range [0, 256] the function encrypts the text by perfomring XOR of all the bytes and the 'key' and returns the resultant"""
    
    return bytes([b ^ key for b in text])

# message = b"Cooking MC's like a pound of bacon"

# encoded_text = single_byte_xor(message, 88)

# decoded_text = single_byte_xor(encoded_text, 88)
