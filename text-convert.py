import sys
if len(sys.argv) == 3:
	with open(sys.argv[1], "r") as input_file:
		with open(sys.argv[2], "w+") as output_file:
			for char in input_file.read():
				if 0 < ord(char) < 256:
					output_file.write(char) 
else:
	print("usage: {} <input file> <output file>".format(sys.argv[0]))
