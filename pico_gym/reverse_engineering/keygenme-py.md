---
Challenge Name: keygenme-py
tags:
  - picoCTF-2021
  - reverse-engineering
Points: "30"
Solves: 26,147
title: ✅ keygenme-py
---
# Description 📄
- [keygenme-trial.py](https://mercury.picoctf.net/static/b016c61bd2cc0be05a59da1dde67a2ac/keygenme-trial.py)

# Method_1 🧪
- check the code

```python
import hashlib

username_trial = "GOUGH"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = ""
key_part_static2_trial = "}"

a = [4, 5, 3, 6, 2, 7, 1, 8]

for i in a:
    key_part_static1_trial += hashlib.sha256(username_trial.encode()).hexdigest()[i]

key_part_static1_trial += key_part_static2_trial
print(key_part_static1_trial)
```
