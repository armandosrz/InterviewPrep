# Arrays

## Strengths and Weaknesses

### Strengths
- Item lookup by index __0(1)__
- Simple data structure with low memory footprint.

### Weaknesses
- Arrays have to be implemented in contiguous memory.
- Adding or deleting elements to the array is O(n), where n is the number of elements in the array.
- Arrays do not allow for the quick rearrangement of elements.
- Searching in the array for an entry with particular attributes is O(n).

## Valuable Tips
- Instead of deleting an entry (_O(N)_ cost to move all elements), try _overwritting_ it. 
- Be confortable working with __subarrays__.
- Be carefull with off by one errors.
- When working on 2-D arrays, use parallel operations.

## Python Specific
- _List_ is dynamically resizing.
- Checking for an element in the array is simple as `a in A`: _O(n)_.
- __Shallow vs Deep Copy__:
  - __Shallow__, contructs a new object and then inserts _references_ into it from the original.
  - __Deep__, inserts _copies_ into it from the original object.
- __bisect__, useful for performing a binary search on a sorted list.


Refer to [code signal](https://app.codesignal.com/interview-practice/topics/arrays/tutorial) for more detail information.