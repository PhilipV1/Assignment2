def first_last(s):
    '''Returns the first and last element of a string'''
    first = s[0]
    last = s[len(s) - 1]
    return first, last


def char_symbol_number(s):
    '''Returns the number of characters, symbols and numbers in given string'''
    symbol_counter = 0
    char_counter = 0
    num_counter = 0

    for element in s:
        if element.isalpha():
            char_counter += 1
        elif element.isdigit():
            num_counter += 1
        else:
            symbol_counter += 1

    return char_counter, symbol_counter, num_counter


def char_types(s):
    '''Returns the number of vowels and consonants in a string'''
    consonants = "lpmknjbhyvgtcfrxdzswq"
    consonant_amount = 0
    vowels = "aeiou"
    vowel_amount = 0

    for char in s:
        if char in vowels:
            vowel_amount += 1
        elif char in consonants:
            consonant_amount += 1

    return vowel_amount, consonant_amount


def main():
    first_string = "Number of vowels and consonants!"
    second_string = "You may not pick 1... You have to pick 2!!"
    # Using casefold function to make all characters lower case
    vowels, consonants = char_types(first_string.casefold())
    chars, symbols, numbers = char_symbol_number(second_string)
    first, last = first_last(first_string)

    print(f"First and last in \"{first_string}\": {first}, {last}")
    print(f"Number of vowels: {vowels}, number of consonants: {consonants}")
    print(f"In the sentence \"{second_string}\" ", end="")
    print(f"the number of letters is {chars}, ", end="")
    print(f"symbols is {symbols} and numbers is {numbers}")


if __name__ == "__main__":
    main()
