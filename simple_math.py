def inc(n):
    '''Increment n with 1'''
    n += 1
    return n


def inc_with(n, t):
    '''Increment n with t'''
    n += t
    return n


def dec(n):
    '''Decrement n with 1'''
    n -= 1
    return n


def dec_with(n, t):
    '''Decrement n with t'''
    n -= t
    return n


def greatest(n1, n2):
    '''Returns the greatest number of n1 and n2.
    Does not check for equal'''
    if n1 > n2:
        return n1
    else:
        return n2


def is_even(n):
    '''Return True if n is even otherwise return False'''
    if n % 2 == 0:
        return True
    else:
        return False


def power(x, n):
    '''Returns X to the power of N'''
    return x**n


def factorial(n):
    '''Recursive function that returns the factorial of n\n
    Reference on factorial and recursion:
    https://www.sciencedirect.com/topics/computer-science/factorial-function'''
    if n == 1:
        return n
    else:
        return (n * factorial(n - 1))


def main():
    print(f"41 plus 1 = {inc(41)}")
    print(f"76 plus 22 = {inc_with(30, 12)}")

    print(f"66 minus 1 = {dec(43)}")
    print(f"143 minus 27 = {dec_with(52, 10)}")

    print(f"Which is greater, 59 or 23?: {greatest(24, 42)}")

    print(f"Is 33 even?: {is_even(42)}")

    print(f"4 to the power of 5 = {power(2, 16)}")

    print(f"Factorial of 6 = {factorial(5)}")


if __name__ == "__main__":
    main()
