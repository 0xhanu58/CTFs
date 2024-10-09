---
title: ✅ Scan Surprise
tags:
  - forensics
  - picoCTF-2024
date: 2024-10-09
difficulty: Easy
---
# Description 📄

I've gotten bored of handing out flags as text. Wouldn't it be cool if they were an image instead? You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_atlas/1/challenge.zip)

The same files are accessible via SSH here: `ssh -p 64401 ctf-player@atlas.picoctf.net` Using the password `83dcefb7`. Accept the fingerprint with `yes`, and `ls` once connected to begin. Remember, in a shell, passwords are hidden!

# Method_1 🧪

- Download `challenge.zip` and unzip it, you'll get a `home` folder

![picoCTF_scan_surprise_img1](https://i.imgur.com/PArNuNv.png)

- Go into the `drop-in` folder, there you'll find `flag.png` 

![picoCTF_scan_surprise_img2](https://i.imgur.com/FyhrrPX.png)

- Now just open the image and scan the **qr code** with your phone and you'll get the **flag**

# Method_2 🧪

- Another option is to use `zbarimg` command from package `zbar-tools` in **debian** systems and `zbar` in **arch** systems to scan the **qr code** in the terminal only

```bash
zbar flag.png
```

![too easy](https://i.imgur.com/21y5T0p.gif)
