# with open("enc", 'r') as f:
#     data = f.read()

# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

data = input("Enter text to be decoded from UTF-16 to UTF-8: ")

data_ord = list(map(ord,list(data)))
data_bin = list(map(bin,data_ord))
data_bin_no_0b = [x[2:] for x in data_bin]
# print(f"{data_bin_no_0b=}\n")

decoded_s = ''

for i in range(0,len(data_ord)):
    decoded_s += chr(data_ord[i] >> 8) + chr(int(data_bin_no_0b[i][-8:],2))

print(f"{decoded_s=}")