"""Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""
def p1(range_max, factor_list):
    range_min = 0
    
    sum_multiples = 0

    for num in range(range_max):
        if num % factor_list[0] == 0:
            sum_multiples = sum_multiples + num
        elif num % factor_list[1] == 0:
            sum_multiples = sum_multiples + num

            # print(num)

    print("Summation of multiples is: %g" % sum_multiples)