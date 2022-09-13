# Program prints the first N primes number based on input


def userinput():
    loop_check = True

    while loop_check:
        try:
            number = int(input("Enter a positive integer: "))

            if number < 0:
                print("Please enter a positive integer!")
            else:
                loop_check = False
        except ValueError:
            print("Please enter a valid integer!")

    return number


# Check if the given number is prime up to sqrt(n)
def isPrime(number):
    if number == 1 or number < 1:
        return False
    if number == 2:
        return True
    if number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, int(number**(1/2) + 1), 2):
            if number % i == 0:
                return False

    return True


# Append the first n primes based on max input
def primeUpTo(max, primeList):
    counter = 1
    number = 3
    primeList.append(2)

    while counter < max:
        if isPrime(number):
            primeList.append(number)
            counter += 1
            number += 2
        else:
            number += 2


def main():
    user_number = userinput()
    primeList = []
    row = 10
    counter = 0

    primeUpTo(user_number, primeList)
    print(f"Length of list: {len(primeList)}")
    for i in range(0, len(primeList)):
        print(primeList[i], end=" ")
        counter += 1
        if counter == row:
            print("")
            counter = 0
    # for i in range (1, len(primeList)):


if __name__ == "__main__":
    main()
