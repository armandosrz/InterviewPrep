from test_framework import generic_test


'''
    I looked a lil to the actual program.
    really straight forward afterwards
'''

def look_and_say(n):
    result = '1'
    def helper(s):
        i, current = 0, []
        while i < len(s):
            count = 1
            while i+1 < len(s) and s[i] == s[i+1]:
                count +=1
                i += 1
            current.append(str(count) + s[i])
            i += 1
        return ''.join(current)
    
    for _ in range(1, n):
        result = helper(result)
    
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
