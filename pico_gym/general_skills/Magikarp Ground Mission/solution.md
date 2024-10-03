---
Challenge Name: Magikarp Ground Mission
tags:
  - picoCTF-2021
  - general-skills
Points: "30"
Solves: 65,569
title: ✅ Magikarp Ground Mission
---
# Description 📄
- Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `abcba9f7`
- Additional details will be available after launching your challenge instance
```bash
sshpass -p 'abcba9f7' ssh ctf-player@venus.picoctf.net -p 49349 -o StrictHostKeyChecking=no
```

# Method_1 🧪
- You can very well **ssh** into the box but i prefer **code**, so check `sol.py` for **solution**