---
Challenge Name: information
tags:
  - picoCTF-2021
  - forensics
Points: "10"
Solves: 105,805
title: ✅ information
---
# Description 📄
- Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/7cf6a33f90deeeac5c73407a1bdc99b6/cat.jpg)
# Method_1 🧪
```bash
exiftool cat.jpg | grep "License" | awk -F":" '{print $2}' | sed 's/ //g' | base64 -d ; echo
```