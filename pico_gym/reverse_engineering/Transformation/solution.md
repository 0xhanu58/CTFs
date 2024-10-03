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

# Reference 📚
https://benjamintoll.com/2022/09/16/on-the-picoctf-transformation-challenge/