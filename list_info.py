import random as rd


def average(array):
    '''Returns the average of the values in the given list'''
    sum = 0

    for value in array:
        sum += value

    return (sum / len(array))


def main():
    # List with 100 elements with values randomized between 1 and 10000
    int_list = [rd.randint(1, 10000) for i in range(0, 100)]
    # Sorting list to access the second largest value easier
    int_list.sort()
    avg = round(average(int_list), 2)
    smallest = min(int_list)
    largest = max(int_list)
    second_largest = int_list[len(int_list) - 2]

    print(f"Largest value in list: {largest}")
    print(f"Smallest value in list: {smallest}")
    print(f"Average value in list: {avg}")
    print(f"Second largest value in list: {second_largest}")


if __name__ == "__main__":
    main()
