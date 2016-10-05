def fact(n):
    '''
    >>> fact(3)
    6
    >>> fact(-1)
    Traceback (most recent call last):
    ...
    ValueError
    
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()