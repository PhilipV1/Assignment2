# Program takes an integer and counts the even, odd and zero digits
def user_input():
    while True:
        try:
            user_input = int(input("Enter a big positive integer"))
            break
        except ValueError:
            print("This is not a valid integer")
        if user_input < 0:
            print("Please enter a positive integer")

    return user_input


def count_digits(num):
    zero = 0
    odd = 0
    even = 0
    # List comprehension to get each single digit
    digit_list = [int(n) for n in str(num)]

    for digit in digit_list:
        if digit == 0:
            zero += 1
        elif digit % 2 == 0:
            even += 1
        else:
            odd += 1

    print(f"Zeroes: {zero}\nOdd: {odd}\nEven: {even}")


def main():
    number = user_input()
    count_digits(number)


if __name__ == "__main__":
    main()
