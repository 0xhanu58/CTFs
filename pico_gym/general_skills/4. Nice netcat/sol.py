from pwn import *

URL = "mercury.picoctf.net" # URL to connecct
PORT = 22902 # Port to connect

p = remote(URL, PORT) # connect to the instance

# print(p.recvall().decode())

received_data = p.recvall().decode()
numbers = list(map(int,received_data.strip().split(' \n')))

print(numbers)

result = ""

for i in range(0,len(numbers)):
    result += chr(numbers[i])

print(result)    

p.close()