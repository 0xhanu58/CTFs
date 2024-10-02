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
