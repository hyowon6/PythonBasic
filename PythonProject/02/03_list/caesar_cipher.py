plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ciphertext=''
for i, ch in enumerate(plaintext):
    # print(i, ch, plaintext[(i+3)%len(plaintext)])
    ciphertext += plaintext[(i+3)%len(plaintext)]

print(ciphertext)
