import base64
import string
with open("the_file", "r") as the_file:
    data = base64.b64decode(the_file.read())



def hamming_distance(x, y):
    # finds the xor of the numbers in the two lists
    list_diff = ["{0:b}".format(i ^ j) for i, j in zip(x, y)]
    # finds the total number of 1's in the XOR's
    return sum([1 for i in "".join(list_diff) if int(i) == 1])

L = []
for KEYSIZE in range(2, 70):
    x = 1
    t=hamming_distance(data[:KEYSIZE], data[KEYSIZE:(x+1)*KEYSIZE])//KEYSIZE
    x+=1
    t+=hamming_distance(data[x*KEYSIZE:(x+1)*KEYSIZE], data[(x+1)*KEYSIZE:(x+2)*KEYSIZE])//KEYSIZE
    # x+=1
    # t+=hamming_distance(data[x * KEYSIZE:(x + 1) * KEYSIZE], data[(x + 1) * KEYSIZE:(x + 2) * KEYSIZE]) // KEYSIZE
    # x+=1
    # t+=hamming_distance(data[x * KEYSIZE:(x + 1) * KEYSIZE], data[(x + 1) * KEYSIZE:(x + 2) * KEYSIZE]) // KEYSIZE
    # x+=1
    # t+=hamming_distance(data[x * KEYSIZE:(x + 1) * KEYSIZE], data[(x + 1) * KEYSIZE:(x + 2) * KEYSIZE]) // KEYSIZE
    # t//=x
    # print(KEYSIZE, t)
    L.append((t, KEYSIZE))

KEYSIZE = min(L)[1]

blocks = [data[i:i+KEYSIZE] for i in range(0, len(data), KEYSIZE)]

for z in range(KEYSIZE):
    answer = []
    strings = {}
    chars = string.ascii_letters + " "
    for i in chars:
        out_arr = []
        for j in [x[z] for x in blocks]:
            out_arr.append(ord(i) ^ j)
        strings[i] = "".join([chr(x) for x in out_arr])
        answer.append((sum([1 for x in out_arr if chr(x) in chars]), ord(i)))
    print(max(answer)[1])
    # print(strings[chr(max(answer)[1])])