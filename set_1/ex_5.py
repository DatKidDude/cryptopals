# Repeating XOR Cipher
from binascii import hexlify

def repeating_key_xor(text: bytes, key: bytes) -> bytes:
    """Encrypt text using a repeated XOR cipher"""

    return bytes([key[idx % len(key)] ^ char for idx, char in enumerate(text)])


if __name__ == "__main__":
    # Line break character needed to match the solution 
    text = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

    key = b"ICE"

    solution = b"0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    
    encoded_text = repeating_key_xor(text, key)
    
    decoded_text = repeating_key_xor(encoded_text, key)
    
    # Verify my solution
    assert hexlify(encoded_text) == solution, "Not equal"

