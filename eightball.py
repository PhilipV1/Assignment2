import random as rd


def rand_strings():
    '''Returns a random string from the list in the function'''
    string_list = [
        "Well of course",
        "Absolutely not",
        "Highly unlikely",
        "I'm not in the mood ask me later",
        "What do you think?",
        "Yes",
        "No",
        "That's a weird question"
    ]
    return string_list[rd.randint(0, len(string_list) - 1)]


def main():
    continue_loop = True

    while continue_loop:
        question = input("Ask the magic 8-ball your question: ")

        if question.casefold() == "stop":
            continue_loop = False
        else:
            print(f"The magic 8-ball says: {rand_strings()}")


if __name__ == "__main__":
    main()
