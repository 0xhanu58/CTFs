---
Challenge Name: Matryoshka doll
tags:
  - picoCTF-2021
  - forensics
Points: "30"
Solves: 42,704
---
# Description
- Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/5eb456e480e485183c9c1b16952c6eda/dolls.jpg)
# Method
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

- check `sol.py` for code