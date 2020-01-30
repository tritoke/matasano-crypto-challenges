import base64
import string
import itertools
with open("6.txt", "r") as the_file:
    b64data = the_file.read().replace("\n", "")
    data = base64.standard_b64decode(b64data)
    print(data)


def hamming_distance(x, y):
    # finds the xor of the numbers in the two lists
    list_diff = ["{0:b}".format(i ^ j) for i, j in zip(x, y)]
    # finds the total number of 1's in the XOR's
    return sum([1 for i in "".join(list_diff) if int(i) == 1])

L = []
for KEYSIZE in range(2, 40):
    x = 1
    t=hamming_distance(data[:KEYSIZE], data[KEYSIZE:(x+1)*KEYSIZE])//KEYSIZE
    x+=1
    t+=hamming_distance(data[x*KEYSIZE:(x+1)*KEYSIZE], data[(x+1)*KEYSIZE:(x+2)*KEYSIZE])//KEYSIZE
    x+=1
    t+=hamming_distance(data[x * KEYSIZE:(x + 1) * KEYSIZE], data[(x + 1) * KEYSIZE:(x + 2) * KEYSIZE]) // KEYSIZE
    x+=1
    t+=hamming_distance(data[x * KEYSIZE:(x + 1) * KEYSIZE], data[(x + 1) * KEYSIZE:(x + 2) * KEYSIZE]) // KEYSIZE
    x+=1
    t+=hamming_distance(data[x * KEYSIZE:(x + 1) * KEYSIZE], data[(x + 1) * KEYSIZE:(x + 2) * KEYSIZE]) // KEYSIZE
    t//=x
    L.append((KEYSIZE, t))

KEYSIZES = [x[0] for x in L if x[1] <= 2]
decrypted_strings = {}
for KEYSIZE in KEYSIZES:
    blocks = [data[i:i+KEYSIZE] for i in range(0, len(data), KEYSIZE)]

    key = ""

    for z in range(KEYSIZE):
        answer = []
        strings = {}
        chars = string.ascii_letters + " "
        for i in chars:
            out_arr = []
            for j in [x[z] for x in blocks if len(x) > z]:
                out_arr.append(ord(i) ^ j)
            strings[i] = "".join([chr(x) for x in out_arr])
            answer.append((sum([1 for x in out_arr if chr(x) in chars]), ord(i)))
        key += chr(max(answer)[1])

    # prints out all of the keys
    print(key, KEYSIZE)

    key_index = 0

    out = []

    decrypted_strings[KEYSIZE] = [chr(int(a) ^ ord(b)) for a, b in zip(data, itertools.cycle(key))]

chars = string.ascii_letters
answer = []
for KEYSIZE in KEYSIZES:
    answer.append((sum([1 for x in decrypted_strings[KEYSIZE] if x in chars]), KEYSIZE))
print(max(answer)[1])
print("".join(decrypted_strings[max(answer)[1]]))
