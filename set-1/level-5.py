important_english = """Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"""

arr = [ord(i) for i in important_english]

answer = """0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""

key =  [ord(i) for i in "ICE"]
key_index = 0

out = []

for i in arr:
    hex_string = format(i ^ key[key_index], "x")
    if len(hex_string) == 1:
        out.append("0" + hex_string)
    else:
        out.append(hex_string)

    key_index += 1
    key_index %= len(key)

out = [str(x) for x in out]

print("".join(out) == answer)

