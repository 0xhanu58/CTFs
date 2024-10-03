---
Challenge Name: Nice netcat...
tags:
  - picoCTF-2021
  - general-skills
Points: "15"
Solves: 125,952
title: ✅ Nice netcat
---
# Description 📄
- There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 22902`, but it doesn't speak English...

# Method_1 🧪
- check the code

```python
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
```