def is_palindrome(n):
    return n == int(str(n)[::-1])

output = list(filter(is_palindrome, range(1,1000)))
print(output)
