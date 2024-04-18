---
Challenge Name: Wave a flag
tags:
  - picoCTF-2021
  - general-skills
Points: "10"
Solves: 153,959
---
# Description
- Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/a00f554b16385d9970dae424f66ee1ab/warm) has extraordinarily helpful information...
# Method 1
```bash
./warm -h
```
# Method 2 (being creative)
```bash
strings warm | grep "CTF" | awk -F":" '{print $2}' | sed 's/ //g'
```
