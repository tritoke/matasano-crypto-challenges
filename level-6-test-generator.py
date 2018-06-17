import sys
import os
import base64

def help():
	print("usage: {} <file> <key>".format(sys.argv[0]))

if len(sys.argv) != 3:
	help()
	sys.exit(1)

try:
	with open(sys.argv[1]) as file:
		data = "".join([i for i in file.read() if 0 < ord(i) < 256])
except OSError as err:
	print("error reading file: {0}".format(err))



arr = [ord(i) for i in data]

key =  [ord(i) for i in sys.argv[2]]
key_index = 0

out = []

for i in arr:
    out.append(i ^ key[key_index])
    key_index += 1
    key_index %= len(key)


with open("outputB64.txt", "w+") as file:
	file.write("".join([chr(i) for i in base64.standard_b64encode(bytes(out))]))

