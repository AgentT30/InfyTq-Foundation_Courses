import sys

# This is to overcome default python recursion limit
sys.setrecursionlimit(10000)


def fibonacci(n):
    FibArray = [0, 1]

    while len(FibArray) < n + 1:
        FibArray.append(0)

    if n <= 1:
        return n
    else:
        if FibArray[n - 1] == 0:
            FibArray[n - 1] = fibonacci(n - 1)

        if FibArray[n - 2] == 0:
            FibArray[n - 2] = fibonacci(n - 2)

    FibArray[n] = FibArray[n - 2] + FibArray[n - 1]
    return FibArray[n]


memo = {}  # global dictionary to store the fibonacci number already computed
print("Fibonacci number:", fibonacci(3))
