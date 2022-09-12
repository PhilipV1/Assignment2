# Sums up all even numbers up to 100 including 100

def main():
    even_array = []
    # Creates a list with all even numbers up to 100
    for i in range(2, 102, 2):
        even_array.append(i)

    print(f"The sum of the even numbers are: {sumEven(even_array)}")


# Calculates the sum of all even numbers up to 100
def sumEven(array):
    sum = 0
    for element in (array):
        sum += element

    return sum


if __name__ == "__main__":
    main()
