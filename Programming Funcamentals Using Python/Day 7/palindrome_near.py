def nearest_palindrome(number):
    # start writitng your code here
    while True:
        if str(number) == str(number)[::-1]:
            return number
        number += 1


number = 12300
print(nearest_palindrome(number))
