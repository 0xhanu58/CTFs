---
Challenge Name: The Numbers
tags:
  - picoCTF-2021
  - cryptography
Points: "50"
Solves: 65,499
title: ✅ The Numbers
---
# Description 📄
- The [numbers](https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png)... what do they mean?

# Method_1 🧪
- If u see the picture then u can see that **some numbers** are there, if u **relate** them to their **position** in **alphabets** like `a - 1`, `b - 2`, `c - 3`, etc. then u'll have the **flag**
- Check the code

```python
def num_to_alphabet(some_list):
    result = ''
    for i in range(len(some_list)):
        if some_list[i].isdigit():
            result += chr(96 + int(some_list[i]))
        else:
            result += some_list[i]

    return result


# direct input from user
input_list = input("Enter numbers seperated by space: ").split(" ")
print(num_to_alphabet(input_list))
```