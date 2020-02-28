""" Optional problems for Lab 3 """

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def is_factor(a):
        if a==1:
            return True
        if n%a==0:
            return False
        else:
            return is_factor(a-1)
    return is_factor(n-1)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if a==b:
        return a
    if a>b and a%b==0:
        return b
    if a<b and b%a==0:
        return a
    def helper(n):
        if min(a,b) % n ==0 and max(a,b) % n ==0:
            return n
        if n == 1:
            return 1
        else:
            return helper(n-1)
    return helper(min(a,b)-1)


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def count_digits(n, a):
        if n==0:
            return 0
        else:
            if n%10==a:
                return count_digits(n//10, a) + 1
            else:
                return count_digits(n//10, a)
    if n<10:
        return 0
    else:
        return ten_pairs(n//10) + count_digits(n//10, 10 - n%10)
