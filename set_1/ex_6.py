import binascii
import sys
from pprint import pprint
from ham_distance import hamming_distance
from ex_3 import brute_force_xor
from ex_5 import repeating_key_xor


def open_file(file_path: str) -> str:
    """Open file and decode it from base64"""
    with open(file=file_path, mode="rb") as f:

        return binascii.a2b_base64(f.read())


def guess_keylength(data: bytes) -> dict:
    """Split the file into chunks of length range and find the hamming distance.
    Return the 4 smallest distances with their associated key.
    """
    results = {}

    for i in range(2, 40):
        keylength = i
        start = 0
        end = start + keylength

        distances = []
        
        # Run until the end of file
        while True:

            # Grab 2 adjacent chunks of data that are KEYLENGTH long.
            first_chunk = data[start:end] 
            second_chunk = data[start + keylength:end + keylength]

            start = end 
            end = start + keylength

            # If the chunks are not equal break
            if len(first_chunk) != len(second_chunk):
                break

            distance = hamming_distance(first_chunk, second_chunk)
            distances.append(distance / keylength)
        
        # Store the keylength and normalized distances 
        results[keylength] = (sum(distances) / len(distances))

    # Get 4 smallest distances
    candidate_keys = dict(sorted(results.items(), key=lambda x: x[1])[:4])

    return candidate_keys


def transpose_blocks(data: bytes, key: int) -> list:
    """Put all bytes that share the same key into a list"""

    keylength = key
    blocks = []
    
    for key in range(keylength):
        chunk = []
        for i in range(key, len(data), keylength):
            # Slice the data so it remains as a bytes object
            chunk.append(data[i:i + 1]) 
        blocks.append(chunk)

    return blocks


def guess_key(blocks: list) -> str:
    """Find the XOR cipher key"""

    key = ""
    for block in blocks:
        hex_string = binascii.hexlify(b"".join(block))
        result = brute_force_xor(hex_string)
        key += result["Key"]

    return key


if __name__ == "__main__":
    file_path = sys.argv[1]
    data = open_file(file_path)

    # Output the top 4 candidate key choices
    candidate_keys = guess_keylength(data)
    print("\n")
    print("*"*8 + "Top 4 Candidate Keys" + "*"*8)
    pprint(candidate_keys, indent=4, sort_dicts=False)
    print("\n")

    # Get the best candidate key
    top_candidate_key = list(candidate_keys.keys())[0]

    blocks = transpose_blocks(data, top_candidate_key)

    key = guess_key(blocks).encode("ascii")
    
    decrypted_data = repeating_key_xor(text=data, key=key)
    print(decrypted_data)