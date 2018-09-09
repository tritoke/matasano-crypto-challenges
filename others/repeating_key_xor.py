from base64 import standard_b64encode as b
from itertools import *
from string import *

fname = input("enter the name of the file you want to encrypt: ")

try:
    data = open(fname, "rb").read()
except (OSError, IOError) as e:
    print("couldn't find file to open :/")
    exit(0)

keyVal = "*" # could be any non alpha numeric character
alnum = digits + ascii_uppercase + ascii_lowercase
isalnum = lambda x: True if sum([1 for i in x if i not in alnum]) == 0 else False
while not isalnum(keyVal): keyVal = input("enter alphanumeric key with which to encrypt the file: ")

key = cycle(bytes(keyVal, "utf-8"))

open("encrypted", "wb").write(b(bytes([i^next(key) for i in data])))
