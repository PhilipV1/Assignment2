import random as rd


def random_num_list(n):
    '''Generates a list of n integers randomized from 0-100'''
    return [rd.randint(0, 100) for i in range(0, n)]


def only_odd(lst):
    '''Returns a new list with only the odd values of given list'''
    return [x for x in lst if x % 2 != 0]


def square(lst):
    '''Returns a new list with the squared values of given list'''
    return [x**2 for x in lst]


def sublist(lst, start, stop):
    temp_list = []
    for i in range(start, stop):
        temp_list.append(lst[i])

    return temp_list


def main():
    num_list = random_num_list(10)
    odd_list = only_odd(num_list)
    square_list = square(num_list)
    sub_list = sublist(num_list, 3, 7)

    print(f"The number list: {num_list}")
    print(f"Odd numbers in list: {odd_list}")
    print(f"Square of each number: {square_list}")
    print(f"The 4 middle values: {sub_list}")


if __name__ == "__main__":
    main()
