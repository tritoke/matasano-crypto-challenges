import aes

a = aes.polynomial(1)

print(a.value)
while True:
    a*=3
    print(hex(a.value))
    if a.value == 1:
        break
