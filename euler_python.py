
def p1(range_max, factor_list):
    """Problem 1
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.

    """
    range_min = 0
    
    sum_multiples = 0

    for num in range(range_max):
        if num % factor_list[0] == 0:
            sum_multiples = sum_multiples + num
        elif num % factor_list[1] == 0:
            sum_multiples = sum_multiples + num

            # print(num)

    print("Summation of multiples is: %g" % sum_multiples)

    return sum_multiples

def p2(max):
    """Problem 2
    Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """

    fib_num = [1,2]
    sum_even = 0
    while fib_num[-1] < max:
        # check if next fibonacci number is even
        if (fib_num[-1] % 2) == 0:
            sum_even = sum_even + fib_num[-1]

        next_num = fib_num[-2]+fib_num[-1]

        fib_num.append(next_num)

    print("Sum of even Fibonacci numbers less than %f is %g" % (max, sum_even))

    return sum_even

def p3(n):
    """Problem 3
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    """
    if n < 2:
        print("No primes less than 2")
        return []

    prime_factors = []

    for p in prime_sieve(int(n/2.0)):
        if p*p > n:
            break
        if n % p == 0:
            prime_factors.append(p)

    return max(prime_factors)

def prime_sieve(n):
    """Sieve of Erathosthenes

    Output the list of all primes less than n
    """

    not_prime = []
    prime = []

    if n < 2:
        print("No primes less than 2")
        return 1

    for i in range(2, n+1):
        if i not in not_prime:
            prime.append(i)
            for j in range(i*i,n+1, i):
                not_prime.append(j)

    return prime
