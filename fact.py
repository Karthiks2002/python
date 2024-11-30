def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series


def sum_of_list(lst):
    return sum(lst)


def main():
    num = int(input("Enter a number to find its factorial: "))
    print(f"The factorial of {num} is {factorial(num)}")

    terms = int(input("Enter the number of terms for the Fibonacci series: "))
    print(f"The Fibonacci series of {terms} terms is: {fibonacci(terms)}")


    numbers = list(map(int, input("Enter the list of numbers (space-separated): ").split()))
    print(f"The sum of the list is: {sum_of_list(numbers)}")


if __name__ == "__main__":
    main()
