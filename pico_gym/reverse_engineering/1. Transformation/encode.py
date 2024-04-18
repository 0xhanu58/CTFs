flag = input("Enter text to be encoded from utf-8 to utf-16: ")

if len(flag)%2!=0:
    print("Retry with even numbered input")
    exit()

encoded_s=''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

print(f"{encoded_s=}")