from threading import Thread


def func1():
    result_sum = 0
    # Write the code to find the sum of numbers from 1 to 10000000
    for i in range(10000000):
        result_sum += i
    print("Sum from func1:", result_sum)


def func2():
    result_sum = 0
    # Write the code to accept 5 numbers from user and find its sum
    for i in range(5):
        result_sum += int(input("Enter next number:"))
    print("Sum from func2:", result_sum)


thread1 = Thread(target=func1)
thread1.start()
thread2 = Thread(target=func2)
thread2.start()
thread1.join()
thread2.join()
