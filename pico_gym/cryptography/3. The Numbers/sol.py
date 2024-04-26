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