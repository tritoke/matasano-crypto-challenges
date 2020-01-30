import string
hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
arr = []
for i in range(0, len(hex_string), 2):
    arr.append(int(hex_string[i] + hex_string[i+1], 16))
answer = []
strings = {}
for i in string.printable:
    out_arr = []
    for j in arr:
        out_arr.append(ord(i) ^ j)
    strings[i] = "".join([chr(x) for x in out_arr])
    answer.append((sum([1 for x in out_arr if chr(x) in string.ascii_letters]), ord(i)))
print(strings[chr(max(answer)[1])])

