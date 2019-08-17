from test_framework import generic_test
import collections

def is_letter_constructible_from_magazine(letter_text, magazine_text):
    letter_text = collections.Counter(letter_text)

    for c in magazine_text:
        if c in letter_text:
            letter_text [c] -= 1
        if letter_text[c] == 0:
            del letter_text[c]
            if not letter_text:
                return True

    return not letter_text


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
