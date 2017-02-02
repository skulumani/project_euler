from euler_python import *

def test_p1_ex():
    assert p1(10,[3 ,5]) == 23

def test_p1_prob():
    assert p1(1000,[3, 5]) == 233168

def test_p2_ex():
    assert p2(100) == 44

def test_p2_prob():
    assert p2(4e6) == 4613732

def test_prime_sieve():
    assert prime_sieve(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_p3_ex():
    assert p3(13195) == 29