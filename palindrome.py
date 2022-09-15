

def is_palindrome(s):
    '''Checks if given string is a palindrome by converting
    the string to all lower case and without spaces'''
    temp_string = ""
    s = s.casefold()
    for element in s:
        if element.isalpha():
            temp_string += element
    # Make a separate reversed string to compare
    comp_string = temp_string[::-1]
    if comp_string == temp_string:
        return True

    return False


def main():
    text_list = ["Ni talar bra latin", "Hello World", "Was it a rat I saw"]

    for element in text_list:
        if is_palindrome(element):
            print(f"{element} is a palindrome")
        else:
            print(f"{element} is not a palindrome")


if __name__ == "__main__":
    main()
