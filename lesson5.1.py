import keyword
import string

user_input = input("Enter a number: ")
new_string_filter = string.punctuation.replace(" ", "")

if not user_input:
    print(False)
elif user_input[0].isdigit():
    print(False)
elif user_input.lower() == user_input:
    print(False)
elif user_input in keyword.kwlist:
    print(False)
elif "__" in user_input:
    print(False)
elif " " in user_input:
    print(False)
else:
    for ele in user_input:
        if ele in string.punctuation:
            print(False)
            break
    else:
        print(True)