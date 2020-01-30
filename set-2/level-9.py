def pkcs7(block, blocklength):
    a = blocklength-len(block)
    return block + bytes([a]*a)

if __name__ == '__main__':
    a = b"YELLOW SUBMARINE"
    print(pkcs7(a,20))
