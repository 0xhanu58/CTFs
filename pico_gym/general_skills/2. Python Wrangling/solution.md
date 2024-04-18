---
Challenge Name: Python Wrangling
tags:
  - picoCTF-2021
  - general-skills
Points: "10"
Solves: 133,016
---
# Description
- Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/ende.py) using [this password](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/pw.txt) to get [the flag](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/flag.txt.en)?
# Method 1
```bash
python3 ende.py -d flag.txt.en dbd1bea4dbd1bea4dbd1bea4dbd1bea4
```
