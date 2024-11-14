from pprint import pprint
from ex_3 import brute_force_xor

def parse_file(file: str) -> dict:
    """Parse each line in the file to find the single byte XOR cipher character.
    Return the metadata of the results
    """

    with open(file, "rb") as f:
        # Split each line and store it in a list
        hex_data = f.readlines()
        
        best_score = 0
        best_result = {}

        for data in hex_data:
            # Strip the newline and carriage return characters
            data = data.rstrip(b"\r\n")
            result = brute_force_xor(data)
            score = result["Score"]
            
            # Update if the result has a better score
            if score > best_score:
                best_score = score
                best_result = result

    return best_result

file_path = input("Enter filename: ")

metadata = parse_file(file_path) 

pprint(metadata)