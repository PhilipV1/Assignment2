from math import sqrt


def distance(x1, x2, y1, y2):
    '''Returns distance with formula:
    sqrt((x1+x2)^2 + (y1+y2)^2)'''
    return sqrt((x1-x2)**2 + (y1-y2)**2)


def user_input(point):
    '''Takes user input for a given point'''
    while True:
        if point == "x1":
            try:
                user_data = float(input("Enter x1: "))
                break
            except ValueError:
                print("Please input a valid float coordinate")
        if point == "x2":
            try:
                user_data = float(input("Enter x2: "))
                break
            except ValueError:
                print("Please input a valid float coordinate")
        if point == "y1":
            try:
                user_data = float(input("Enter y1: "))
                break
            except ValueError:
                print("Please input a valid float coordinate")
        if point == "y2":
            try:
                user_data = float(input("Enter y2: "))
                break
            except ValueError:
                print("Please input a valid float coordinate")
    return user_data


def main():
    x1 = user_input("x1")
    x2 = user_input("x2")
    y1 = user_input("y1")
    y2 = user_input("y2")

    print(f"Distance between ({x1}, {y1}) and ({x2}, {y2}) is: ", end="")
    dist = distance(x1, x2, y1, y2)
    print("%.3f" % dist)  # Float formating


if __name__ == "__main__":
    main()
