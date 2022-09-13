import random as rd


def userInput():
    loop_check = True

    while loop_check:
        try:
            input_string = "Enter number of integers to be generated: "
            user_input = int(input(input_string))
            if user_input < 1:
                print("Please input a value greater than 0")
            else:
                loop_check = False
        except ValueError:
            print("Please enter a valid integer")

    return user_input


def main():
    amount = userInput()
    maximum = 0
    minimum = 100
    average = 0
    current = 0

    print("Generated values: ", end="")
    for i in range(0, amount):
        current = rd.randint(1, 100)
        average += current

        if current < minimum:
            minimum = current
        if current > maximum:
            maximum = current

        print(current, end=" ")

    average /= amount

    print(f"\nAverage, min and max are: {average}, {minimum}, {maximum}")


if __name__ == "__main__":
    main()
