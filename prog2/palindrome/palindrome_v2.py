def is_palindrome_v2(s):
    """ (str) -> boolean

    Return True if the input string is a palindrome

    >>> is_palindrome_v2('noon')
    True
    >>> is_palindrome_v2('racecar')
    True
    >>> is_palindrome_v2('dented')
    False
    """

    ###Compare first half of string vs. reverse(2nd half string)

    n = len(s)
    return s[:n//2] == reverse(s[n - n//2:])

def reverse(s):
    """ (str) -> str

    Return the reverse of the input string

    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    """

    rev = ''
    for ch in s:
        rev = ch + rev
    return rev


