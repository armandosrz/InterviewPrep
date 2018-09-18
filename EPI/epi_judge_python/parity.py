from test_framework import generic_test

'''
The parity of a binary word is 1 if the number of 1s is odd
otherwise it is 0.

Compute parity of a really long 64-bit word.

'''

def parity(x):
    '''
    ones = ''.join(filter(lambda y: y == '1', bin(x)))
    return len(ones) % 2
    '''
    result = 0
    while x:
        result ^= 1
        x &= x -1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
