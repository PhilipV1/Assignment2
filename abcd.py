def get_number(a, b, c, d):
    '''Converting the list of numbers into a single int'''
    abcd = (a * 1000) + (b * 100) + (c * 10) + d

    return abcd


def find_digits():
    '''Calculates the  four digit palindromic number'''
    number = 0
    a = 0
    b = 0
    c = 0
    d = 0

    # We know that 'a' can only be 1 or 2 otherwise 'd' > 10
    for thousand in [1, 2]:
        a = thousand

        for hundred in range(0, 10):
            b = hundred

            for ten in range(0, 10):
                c = ten

                for one in [4, 8]:
                    # Because 'a' is either 1 or 2 'd' has to be 4 or 8
                    d = one
                    number = get_number(a, b, c, d)
                    reverse = get_number(d, c, b, a)
                    if number * 4 == reverse:
                        return number

    return number


def main():
    digits = find_digits()

    print(f"The four digit number is: {digits}")


if __name__ == "__main__":
    main()
