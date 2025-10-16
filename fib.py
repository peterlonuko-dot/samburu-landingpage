from functools import lru_cache
@lru_cache(maxsize=None)
def slow_fib(n):
    if n == 1 or n == 2:
        return 1
    else: 
        return slow_fib(n-1) + slow_fib(n-2)
#for loop to repeat call to slow fib x times   
for n in range(1,101):
    print(n,":", slow_fib(n))

                                       