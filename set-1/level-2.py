hex_string = "1c0111001f010100061a024b53535009181c"
dec_string = "686974207468652062756c6c277320657965"

arr1 = []
arr2 = []


for i in range(0, len(hex_string), 2):
    arr1.append(int(hex_string[i] + hex_string[i+1], 16))
    arr2.append(int(dec_string[i] + dec_string[i+1], 16))


def xor(arr1, arr2):
    return_arr = []
    for i, j in zip(arr1, arr2):
        return_arr.append(i ^ j)
    return "".join([hex(i) for i in return_arr])

print(xor(arr1, arr2))

