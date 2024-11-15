# Script to fuck around on
from binascii import a2b_base64
from ex_6 import hamming_distance

x = b"HUIfTQsPAh9PE048GmllH0kcDk4TAQsHThsBFkU2AB4BSWQgVB0dQzNTTmVS"
y = b"BgBHVBwNRU0HBAxTEjwMHghJGgkRTxRMIRpHKwAFHUdZEQQJAGQmB1MANxYG"

# Decode text from base64
x = a2b_base64(x)
y = a2b_base64(y)

# Calculate hamming distance
keysize = 3

# Step 1: Divide the cipher text into blocks of length equal to the key size guessed above
chunk_x = [x[i:i + keysize] for i in range(0, len(x), keysize)]
chunk_y = [y[j:j + keysize] for j in range(0, len(y), keysize)]

# Step 2: Calculate the Hamming distance by dividing it by the key size
distances = []
for i, j in zip(chunk_x, chunk_y):
    distances.append(hamming_distance(i, j))

# Step 3: Normalize the distance by dividing it by the key size (Repeat for 4 to 5 blocks)
normalized_distances = list(map(lambda x: x / keysize, distances))

# Step 4: Take the average of the calculated distances
average_distance = sum(normalized_distances) / keysize
print(average_distance) 

