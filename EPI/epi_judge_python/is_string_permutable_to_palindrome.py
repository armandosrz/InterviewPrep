from test_framework import generic_test

import collections

def can_form_palindrome(s):
    # a string can be permutated to a palindrome if and only if
    # the number of odd occurances is at most one
    counts = collections.Counter(s)
    return sum( c % 2 for c in counts.values()) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
