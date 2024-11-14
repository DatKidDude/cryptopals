from binascii import unhexlify
from ex_3 import brute_force_xor

# TODO: Put this into a function
with open("data.txt", "rb") as file:
    hex_data = file.readlines()
    
    best_score = 0
    best_result = {}

    for data in hex_data:
        data = data.rstrip(b"\r\n")
        result = brute_force_xor(data)
        score = result["Score"]
        
        if score > best_score:
            best_score = score
            best_result = result

    print(best_result)


