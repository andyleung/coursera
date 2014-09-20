def is_palindrome_v3(s):
    """ (str) -> boolean

    Return True if the input string is a palindrome

    >>> is_palindrome_v3('noon')
    True
    >>> is_palindrome_v3('racecar')
    True
    >>> is_palindrome_v3('dented')
    False
    """

    ## Use i and j as the index of the input string

    i = 0
    j = len(s) - 1

    while i < j and s[i] == s[j]:
        i = i + 1
        j = j - 1

    return i >= j


