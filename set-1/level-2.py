hex_string = "1c0111001f010100061a024b53535009181c"
dec_string = "686974207468652062756c6c277320657965"
answer = "746865206b696420646f6e277420706c6179"
arr1 = []
arr2 = []


for i in range(0, len(hex_string), 2):
    arr1.append(int(hex_string[i] + hex_string[i+1], 16))
    arr2.append(int(dec_string[i] + dec_string[i+1], 16))


def xor(arr1, arr2):
    return_arr = []
    for i, j in zip(arr1, arr2):
        return_arr.append(format(i^j, "x"))
    return "".join(return_arr)

print(xor(arr1, arr2) == answer)

