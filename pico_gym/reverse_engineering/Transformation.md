---
Challenge Name: Transformation
tags:
  - picoCTF-2021
  - reverse-engineering
Points: "20"
Solves: 50,651
title: ✅ Transformation
---
# Description 📄
- I wonder what this really is... [enc](https://mercury.picoctf.net/static/0d3145dafdc4fbcf01891912eb6c0968/enc) 
`''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`

# Method_1 🧪
- Go to **cyberchef** and use **magic** with intense mode, there you will get the **flag** and get the **unicode type** `utf-16-be`
```python
with open("enc", 'r') as f:
    data = f.read()

print(data.encode('utf-16-be').decode())
```

# Method_2 🧪
- Check `decode.py`, i was having fun so also created `encode.py`

## Decode.py
- Code:

```python
# with open("enc", 'r') as f:
#     data = f.read()

# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

data = input("Enter text to be decoded from UTF-16 to UTF-8: ")

data_ord = list(map(ord,list(data)))
data_bin = list(map(bin,data_ord))
data_bin_no_0b = [x[2:] for x in data_bin]
# print(f"{data_bin_no_0b=}\n")

decoded_s = ''

for i in range(0,len(data_ord)):
    decoded_s += chr(data_ord[i] >> 8) + chr(int(data_bin_no_0b[i][-8:],2))

print(f"{decoded_s=}")
```

## Encode.py
- Code:

```python
flag = input("Enter text to be encoded from utf-8 to utf-16: ")

if len(flag)%2!=0:
    print("Retry with even numbered input")
    exit()

encoded_s=''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

print(f"{encoded_s=}")
```

# Reference 📚
https://benjamintoll.com/2022/09/16/on-the-picoctf-transformation-challenge/