from test_framework import generic_test

'''
  Problem:
  Given n, return all primes up to and including n.

  Notes: 
  A prime is a number that is not equal to 1 and is only
  divisibale by itself. 
  - As we generate them, we know that multiples of previous
    primes are not valid. 
  
  Approach 1:
  - Make a boolean list of candidates up to N. Mark all as true.
  - In each iteration, check if the number is still a valid candidate.
  - If it is, mark all possible multiples < n as false.
  - All multiples can be obtain by adding a prime to itself constantly
  *** This will avoid doing checks for numners already marked as not
      candidates.
  - eficiency 0(n log log n) p. 55
'''
def generate_primes(n):
    candidate = [True] * (n+1)
    result = []
    for x in range(2, n+1):
        if candidate[x]:
            result.append(x)
            multiples = x + x
            while multiples <= n:
                candidate[multiples] = False 
                multiples += x
                

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
