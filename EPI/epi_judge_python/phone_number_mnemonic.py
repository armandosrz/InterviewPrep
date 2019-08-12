from test_framework import generic_test, test_utils



'''
    Solution:

    Go through every single posible permutation using recursion.

    We use a temp array in which we store all the changes to specific 
    indexes. Base case ? when we digit number reaches the specific len.

    Important to study the recursion big O notations.
'''

# The mapping from digit to corresponding characters.
MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

def phone_mnemonic(phone_number):
    def helper(digit):
        if digit == len(phone_number):
            result.append(''.join(temp))
        else:
            for c in MAPPING[int(phone_number[digit])]:
                temp[digit] = c
                helper(digit +1)

    result, temp = [], [0]* len(phone_number)
    helper(0)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
