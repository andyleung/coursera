def is_palindrome_v1(s):
    """ (str) -> boolean

    Return True if the input string is a palindrome

    >>> is_palindrome_v1('noon')
    True
    >>> is_palindrome_v1('racecar')
    True
    >>> is_palindrome)v1('dented')
    False
    """

    return s == reverse(s)

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


