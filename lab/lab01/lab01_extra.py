"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    product = n
    if k<=0:
        return 1
    if k==1:
        return n
    if k>1:
        while k>1:
            product = product * (n-1)
            n = n-1
            k= k-1
        return product

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """

    while n>10:
        digit= n % 10
        n = (n - digit)//10
        if digit==8:
            next_d = n % 10
            if next_d==8:
                return True
    else:
        return False
