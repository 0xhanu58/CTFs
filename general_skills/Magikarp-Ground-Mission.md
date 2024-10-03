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
- You can very well **ssh** into the box but i prefer **code**, so check code for **solution**

```python
import paramiko

# Create an SSH client instance
ssh_client = paramiko.SSHClient()

# Automatically add host keys
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the SSH server
hostname = 'venus.picoctf.net'
port = 49349  # Default SSH port is 22
username = 'ctf-player'
password = 'abcba9f7'

ssh_client.connect(hostname, port, username, password)

# Perform SSH commands
stdin, stdout1, stderr = ssh_client.exec_command('cat /home/ctf-player/drop-in/1of3.flag.txt')
stdin, stdout2, stderr = ssh_client.exec_command('cat /2of3.flag.txt')
stdin, stdout3, stderr = ssh_client.exec_command('cat /home/ctf-player/3of3.flag.txt')

# Print the output of the command
flag1 = stdout1.read().strip()
flag2 = stdout2.read().strip()
flag3 = stdout3.read().strip()

print((flag1 + flag2 + flag3).decode())

# Close the SSH connection
ssh_client.close()
```