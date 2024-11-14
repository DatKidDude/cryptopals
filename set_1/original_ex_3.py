# My original implementation of set 1 exercise 3
# Just wanted to keep it 

from binascii import a2b_hex, unhexlify
import string
from xor_cipher import single_byte_xor
from pprint import pprint

ciphertext = b"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def brute_force_xor(cipher):

    unhex = list(unhexlify(cipher))

    last_score = 0
    best_score = 0
    character = None

    for num in range(2 ** 8):
        for char in unhex:
            if (chr(num ^ char).upper()) in string.ascii_uppercase + " ":
                last_score += 1
            else:
                continue
        
        last_score /= (len(cipher) // 2)
        if (last_score) > .7 and last_score > best_score:
            best_score = last_score
            character = chr(num)
        
        last_score = 0

    return {
        "Best Score:": best_score,
        "Ascii Number:": ord(character),
        "Character:": character,
        "Decoded Text:": single_byte_xor(a2b_hex(cipher), ord(character)),
    }


result = brute_force_xor(ciphertext)
pprint(result)
