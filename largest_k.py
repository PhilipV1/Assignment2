# This program calculates arithmetic progression based on input value

# Function takes an input value with type int
def userInput():
    loop_check = True

    while loop_check:
        try:
            user_input = int(input("Enter a positive integer: "))
            loop_check = False
        except ValueError:
            print("Please enter an integer!")

    return user_input


# Calculates the largest number in arithmetic progression
def arithmeticProgression(number):
    max = 0
    current = 0
    previous = 0
    sum = 0

    while sum < number:
        sum += current
        if sum >= number:
            max = previous
        else:
            previous = current
        current += 2

    return max


def main():
    input = userInput()
    largest = 0

    if input < 0:
        print("Integer is not positive. Program terminating!")
        exit()
    else:
        largest = arithmeticProgression(input)
        if largest > 8:
            print(f"{largest} is the largest K such that 0+2+4+6+..", end="")
            print(f"{largest} < {input}")
        else:
            print(f"{largest} is the largest K such that ", end="")
            for i in range(0, largest, 2):
                print(f"{i}+", end="")
            print(f"{largest} < {input}")


if __name__ == "__main__":
    main()
