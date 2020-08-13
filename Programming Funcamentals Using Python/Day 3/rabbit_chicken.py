
def solve(heads, legs):
    error_msg = "No solution"
    chicken_count = 0
    rabbit_count = 0

    for i in range(heads+1):
        j = heads-i
        if (2*i)+(4*j) == legs:
            chicken_count = i
            rabbit_count = j
            print(chicken_count, rabbit_count)
            return
        else:
            print(error_msg)
            return


# Provide different values for heads and legs and test your program
solve(2, 8)
