from gmpy2 import *

def rot_decode(rot_num,text):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the position of the character in the alphabet
            offset = ord('a') if char.islower() else ord('A')
            # Apply the ROT13 transformation
            rotated = (ord(char) - offset + rot_num + 1) % 26 + offset - 1
            result += chr(rotated)
        else:
            result += char
    return result

def rot_encode(rot_num,text):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the position of the character in the alphabet
            offset = ord('a') if char.islower() else ord('A')
            rotated = ord(char) - offset + 1 - rot_num
            if rotated>=0:
                result += chr(rotated + offset - 1)
            elif rotated<0:
                result += chr((26 + rotated) + offset - 1)
        else:
            result += char
    return result 


def main():
    c = input("Type (e)ncode and (d)ecode: ")
    user_input = input("Enter text to be encoded/decoded: ")
    rot_num = int(input("Enter rot-number: "))
    if c=='e':
        result = rot_encode(rot_num,user_input)
        print(f"ROT{rot_num} encoded:", result)
    elif c=='d':
        result = rot_decode(rot_num,user_input)
        print(f"ROT{rot_num} decoded:", result)
    else:
        print("Enter either 'e' for encode or 'd' for decode.")

if __name__ == "__main__":
    main()
