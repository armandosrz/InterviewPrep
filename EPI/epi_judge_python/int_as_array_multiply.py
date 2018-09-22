from test_framework import generic_test

'''
    Problem:
    Write a program that takes two arrays of digits that represent a non-negative
    integer. Write a program that will multiply them
    Ex. <1,2,9> and <1,0> will return <1,2,9.0>

    Notes:
    - In a brute force fashion we could transform to integers an multiply them, 
    and return a new list.

    This is the solution from the book. I was trying to reinvent the wheel in this
    one. 

    - In order to make the tracking easier, it is always better to reverse the 
      order of this arrays when working through this

'''

def multiply(num1, num2):
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i+j + 1] %= 10

    result = result[next((i for i, x in enumerate(result) if x!= 0), len(result)):] or [0]

    return [ sign * result[0]] + result[1:]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
