NUM_REPS = 100000000

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
    
    print('Calculated_value:', (sum/NUM_REPS)*4)


if __name__=='__main__':
    calculate_pi()
