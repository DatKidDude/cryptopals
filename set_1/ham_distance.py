# Cracking repeating-key XOR cipher (It's on now)

# Guessed length of the key
keysize = range(2, 41)

def hamming_distance(str1: bytes, str2: bytes) -> int:
    """Measures the hamming distance between two strings of equal length. Converts both strings to their binary values and then does and XOR computation to find the difference in the bit values."""

    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")
    
    # Turn characters into their binary values
    # str1_bits = "".join([f"{i:08b}" for i in str1]).encode("ascii")
    # str2_bits = "".join([f"{i:08b}" for i in str2]).encode("ascii")

    # return sum(ch1 != ch2 for ch1, ch2 in zip(str1_bits, str2_bits))
    return sum(bin(b1 ^ b2).count("1") for b1, b2 in zip(str1, str2))


if __name__ == "__main__":
    str1 = b"this is a test"
    str2 = b"wokka wokka!!!"
    
    differing_bits = hamming_distance(str1, str2)
    print(differing_bits)
    # Verify the hamming distance is 37 
    assert differing_bits == 37, "Hamming distance is incorrect"