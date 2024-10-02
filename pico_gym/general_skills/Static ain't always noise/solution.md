---
Challenge Name: Static ain't always noise
tags:
  - picoCTF-2021
  - general-skills
Points: "20"
Solves: 75,714
title: ✅ Static ain't always noise
---
# Description 📄
- Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/ff4e569d6b49b92d090796d4631a2577/static)? This [BASH script](https://mercury.picoctf.net/static/ff4e569d6b49b92d090796d4631a2577/ltdis.sh) might help!
# Method_1 🧪
```bash
strings -a static | grep "picoCTF"
```

# Method_2 🧪
```bash
./ltdis.sh static && cat static.ltdis.strings.txt
```