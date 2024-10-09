---
title: Verify
tags:
  - forensics
  - picoCTF-2024
Date: 2024-10-08
Difficulty: Easy
---
# Description 📄

People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate. You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_rhea/10/challenge.zip)

The same files are accessible via SSH here: `ssh -p 59454 ctf-player@rhea.picoctf.net` Using the password `83dcefb7`. Accept the fingerprint with `yes`, and `ls` once connected to begin. Remember, in a shell, passwords are hidden!

- Checksum: 467a10447deb3d4e17634cacc2a68ba6c2bb62a6637dad9145ea673bf0be5e02
- To decrypt the file once you've verified the hash, run `./decrypt.sh files/<file>`.

# Method_1 🧪

- Download the `.zip` file and `unzip` it, you will get a `home` folder

```bash
unzip challenge.zip
```

<img src="https://i.imgur.com/ZPZcjU7.png" alt="picoCTF_verify_img1" title="picoCTF_verify_img1" width=650/>

- Go in `drop-in` folder where you'll find `decrypt.sh`, `checksum.txt` and a `files` folder containing many files with random names

![picoCTF_verify_img2](https://i.imgur.com/NQVI9Ce.png)

- If we go according to the challenge description then we have a checksum hash and many files so we can verify which file does that checksum belong to. Since it is given that `SHA-256` is used then we'll also use that

```bash
sha256sum files/*  | grep $(cat checksum.txt)
```

![picoCTF_verify_img3](https://imgur.com/LLtpNII.png)

- Now all that is left is to **decrypt** this file, if we look into `decrypt.sh` we'll find the following command its using to decrypt

```bash
openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -salt -in "/home/ctf-player/drop-in/$file_name" -k picoCTF
```

- Just modify it a little to **decrypt** our file and get the flag

```bash
openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -salt -in "files/c6c8b911" -k picoCTF
```