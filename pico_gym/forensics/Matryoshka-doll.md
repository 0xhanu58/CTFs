---
Challenge Name: Matryoshka doll
tags:
  - picoCTF-2021
  - forensics
Points: "30"
Solves: 42,704
title: ✅ Matryoshka doll
---
# Description 📄
- Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/5eb456e480e485183c9c1b16952c6eda/dolls.jpg)

# Method_1 🧪
- Run
```bash
binwalk -e dolls.jpg
```

- From this u will get `2_c.jpg`, do same for `2_c.jpg` and repeat the process untill you extract `4_c.jpg` with
```bash
binwalk -e 4_c.jpg
```

- From there you'll get `flag.txt` in binary form
```bash
xxd -c1 -p flag.txt | sed '/^00$/d' | xxd -r -p
```

- check the code

```python
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
```