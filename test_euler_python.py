from euler_python import *
import numpy as np

def test_p1_ex():
    assert p1(10,[3 ,5]) == 23

def test_p1_prob():
    assert p1(1000,[3, 5]) == 233168

def test_p2_ex():
    assert p2(100) == 44

def test_p2_prob():
    assert p2(4e6) == 4613732

def test_prime_sieve_erathosthenes():
    np.testing.assert_allclose(prime_sieve_erathosthenes(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

def test_primesfrom2to():
    np.testing.assert_allclose(primesfrom2to(30),[2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

def test_p3_ex():
    np.testing.assert_allclose(p3(13195),29)
    