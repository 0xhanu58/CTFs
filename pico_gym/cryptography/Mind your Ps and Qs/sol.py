from factordb.factordb import FactorDB
from gmpy2 import *

c = 240986837130071017759137533082982207147971245672412893755780400885108149004760496
n = 831416828080417866340504968188990032810316193533653516022175784399720141076262857
e = 65537

f = FactorDB(n)
f.connect()

p,q = f.get_factor_list()
ph = (p-1)*(q-1)
d = invert(e, ph)
plaintext = pow(c,d,n)

print(f"{plaintext=}")
print("Flag: {}".format(bytearray.fromhex(format(plaintext, 'x')).decode()))

plaintext_ascii = ''

while plaintext > 0:
    plaintext_ascii += chr(plaintext & 0xFF)
    plaintext >>= 8

plaintext_ascii = plaintext_ascii[::-1]

print(f"{plaintext_ascii=}")