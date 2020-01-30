import base64
hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
answer = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
arr = []
for i in range(0, len(hex_string), 2):
    arr.append(int(hex_string[i] + hex_string[i+1], 16))

print(base64.b64encode(bytes(arr)) == answer)