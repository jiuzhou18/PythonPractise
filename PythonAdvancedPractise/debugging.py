def foo(s):
    n = int(s)
    assert n!=0, "Error: the divisor is zero!"
    return 10/n

foo('0')