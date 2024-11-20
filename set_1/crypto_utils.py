# Cryptopals utility functions
import string
from binascii import unhexlify



def english_score(text: bytes) -> int:
    """Scores text based on the frequency of common English characters. """

    score = 0
    # Only use most common characters to prevent false positives
    common_chars = b"etaoin shrdlu"

    for char in text.lower():
         if chr(char) in string.printable:
             if char in common_chars:
                score += 1

    return score


def brute_force_xor(cipher: bytes) -> dict:
    """Brute forces single byte XOR cipher by testing each possible key."""
    hex_bytes = unhexlify(cipher)

    best_score = 0
    best_result = {}

    # Loop through all all ascii values
    for key in range(256):
        decoded_text = single_byte_xor(hex_bytes, key)
        score = english_score(decoded_text)

        # Update if the key has a better score
        if score > best_score:
            best_score = score
            best_result = {
                "Cipher": cipher,
                "Score": best_score,
                "Ascii Number": key,
                "Key": chr(key),
                "Decoded Text": decoded_text,
            }

    return best_result


def single_byte_xor(text: bytes, key: int) -> bytes:
    """Given a plain text 'text' as bytes and an encryption key 'key' as a byte in range [0, 256] the function encrypts the text by perfomring XOR of all the bytes and the 'key' and returns the resultant"""
    
    return bytes([b ^ key for b in text])