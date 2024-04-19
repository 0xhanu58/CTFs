with open("flag.txt", "rb") as file:
    f = file.read()



# METHOD-1 (direct)
result = ''
print(f"{list(f)=}")
for i in f:
    if i!=0:
        result += chr(i)

print(f"{result=}\n")



# METHOD-2 (using hex)
import binascii

result2 = ''
hex_string_of_flag  =  binascii.hexlify(f).decode()
print(f"{hex_string_of_flag=}")

for i in range(0,len(hex_string_of_flag),4):
    result2 += chr(int(hex_string_of_flag[i] + hex_string_of_flag[i+1],16))

print(f"{result2=}")