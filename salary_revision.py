def average(salaries):
    '''Calculates the average of given salaries'''
    avg = 0

    for x in salaries:
        avg += x

    return (avg / len(salaries))


def median(salaries):
    '''Calculates the median of given salaries'''
    if len(salaries) % 2 != 0:
        return salaries[(len(salaries)//2)]
    else:
        # If there is an even length it takes the average of the middle two
        first_median = salaries[(len(salaries)//2) - 1]
        second_median = salaries[(len(salaries) // 2)]
        return (first_median + second_median) / 2


def gap(salaries):
    '''Calculates the gap between highest and lowest salary'''
    gap = max(salaries) - min(salaries)
    return gap


def main():
    # Takes several salary inputs and splits them using whitespace
    salary_input = input("Enter salaries separated by one whitespace: ")
    salaries = salary_input.split()
    # Creating a new list with all the salaries and sort it
    salary_list = [int(x) for x in salaries]
    salary_list.sort()

    salary_gap = round(gap(salary_list))
    salary_average = round(average(salary_list))
    salary_median = round(median(salary_list))

    print(f"Median: {salary_median}")
    print(f"Average: {salary_average}")
    print(f"Gap: {salary_gap}")


if __name__ == "__main__":
    main()
