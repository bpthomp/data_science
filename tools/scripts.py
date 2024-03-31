NUM_REPS = 10000

import random 
from math import sqrt

def calculate_pi(reps=NUM_REPS):
    
    # intiialize all samples
    samples = [0]*reps
    sum = 0

    for i in range(len(samples)):
        samples[i] = tuple([random.random(), random.random()])
        x , y = samples[i]
        if sqrt(x**2 + y**2) < 1:
            sum +=1
    
    print('Calculated value:', (sum/NUM_REPS)*4)

def calculate_pi_leibniz(reps=NUM_REPS):

    # initialize denominator and estimate
    denom = 1
    sum = 0

    for i in range(reps):
        
        # increment so this isn't negative
        i+=1

        if i % 2:
            sum += 4/denom
        else:
            sum -= 4/denom
        denom += 2

    print('Calculatd Leibniz value', sum)

"""
Permutations and Combinations
* Rule of thumb - divide by the thing you don't care about
"""

# recursion for factorial
def factorial(n):
    if n==1:
        return n
    else: 
        return n*factorial(n-1)

def permutation_no_repetition(n, r):
    return factorial(n)/factorial(n-r)

def permutation_with_repetition(n,r):
    return n**r

def combination_no_repetition(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

def combination_with_repetition(n,r):
    return factorial(n+r-1)/(factorial(r)*factorial(n-1))


def coin_flip(reps):
    heads = 0
    for i in range(reps):
        if random.random()<=0.5:
            heads += 1
    return(heads)

if __name__=='__main__':
    calculate_pi()
    calculate_pi_leibniz()
    print('combination with repetition of 10,4:', combination_with_repetition(10,4))
    print('number of heads after fipping 10:', coin_flip(10))