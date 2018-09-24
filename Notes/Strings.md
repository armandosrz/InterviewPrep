# Strings

## Valuable Tips
- Similar to arrays, most problems have a brute-force solution. 
- Updating a string from the front is slow (need to shift all chars to the back), try 
  doing it from the back.
- If you will perform multiple mutations, working with a _list_ is less expensive.

## Python Specific
- _Strings_ are inmutable, try avoiding adding single chars if possible
- Checking for an element in the array is simple as `a in A`: _O(n)_.


## Common problems

### Palindorme 

```python3

def is_palindrome(s):
    return all(s[i] == s[~i] for i in (len(s) // 2))
```
