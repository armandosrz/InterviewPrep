import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a string encoded as bytearray.
def reverse_words(s):
    return ' '.join(reversed(s.split(' ')))


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s = executor.run(functools.partial(reverse_words, s))

    return s


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
