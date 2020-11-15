import time
text = input("enter string: ")
alpha="abcdefghijklmnopqrstuvwxyz"
s = int(input("Enter first shift number: "))
q = int(input("Enter second shift number: "))
start = time.time()
original = ''


for char in alpha:
    original = original + chr((ord(char) + s - 97) % 26 + 97)


print (alpha)
print(original)
beta = original
original = ''
for char in text:
    original = original + chr((ord(char) + s - 97) % 26 + 97)

print("original string: ", text)
print("original Ceaser cypher text: ", original)
sudo_string = list(original)

psudo_string =list(beta)
leng = len(sudo_string)
size = len(psudo_string)

total = s * q
if (total % 2) == 0:
    for i in range(0, leng):
        if i % 2 == 0:
            sudo_string[i] = chr((ord(sudo_string[i]) + q))
    print('The Final Cipher text is: ', *sudo_string)

else:
    for i in range(0, leng):
        if i % 2 != 0:
            sudo_string[i] = chr((ord(sudo_string[i]) + q))
    print('The Final Cipher text is: ', *sudo_string)


    ################################################
if (total % 2) == 0:
    for i in range(0, size):
        if i % 2 == 0:
            psudo_string[i] = chr((ord(psudo_string[i]) + q))
    print('The Final Cipher text is: ', *psudo_string)

else:
    for i in range(0, size):
        if i % 2 != 0:
            psudo_string[i] = chr((ord(psudo_string[i]) + q))
    print('The Final Cipher text is: ', *psudo_string)

    ################################################
if (total % 2) == 0:
    for i in range(0, leng):
        if i % 2 == 0:
            sudo_string[i] = chr((ord(sudo_string[i]) - q))
    print('Decryption using key 2 results in : ', *sudo_string)

else:
    for i in range(0, leng):
        if i % 2 != 0:
            sudo_string[i] = chr((ord(sudo_string[i]) - q))
    print('Decryption using key 2 results in : ', *sudo_string)
#####################################################
if (total % 2) == 0:
    for i in range(0, size):
        if i % 2 == 0:
            psudo_string[i] = chr((ord(psudo_string[i]) - q))
    print('Decryption using key 2 results in : ', *psudo_string)

else:
    for i in range(0, size):
        if i % 2 != 0:
            psudo_string[i] = chr((ord(psudo_string[i]) - q))
    print('Decryption using key 2 results in : ', *psudo_string)

#####################################################
decrypt = ""
for x in sudo_string:
    decrypt += x

for char in decrypt:

    decrypt = decrypt + chr((ord(char) - s - 97) % 26 + 97)
    power = decrypt[leng:]
##########################################################

decrypt1 = ""
for x in psudo_string:
    decrypt1 += x

for char in decrypt1:

    decrypt1 = decrypt1 + chr((ord(char) - s - 97) % 26 + 97)
    power1 = decrypt1[size:]

###########################################
print('Decrypted Alphabets A-Z: ', power1)
print('The Decrypted Message is :', power)

end = time.time()
print('Execution time:', end - start)
input("Press Enter to exit")
