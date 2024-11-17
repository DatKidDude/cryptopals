# # Script to fuck around on
import binascii
from pprint import pprint
from ham_distance import hamming_distance


def guess_keylength(file: str):
    with open("data6.txt", "rb") as f:
        data = binascii.a2b_base64(f.read())

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


candidate_keys = guess_keylength("data6.txt")
print("\n")
print("*"*8 + "Top 4 Candidate Keys" + "*"*8)
pprint(candidate_keys, indent=4, sort_dicts=False)
print("\n")