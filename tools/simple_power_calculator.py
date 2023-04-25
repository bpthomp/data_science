import pandas as pd
import numpy as np
import scipy.stats as stats

class DiffinMeansPowerCalculator:
    '''This class uses 
    simple heuristics to get different kinds of 
    power analysis, such as equal cost of 
    partitioning observations into 
    treatment or control groups and equal 
    variance of the outcome across 
    the two groups. 

    Reference: https://www.nber.org/system/files/working_papers/w15701/w15701.pdf
    
    Parameters:
        alpha: Probability of committing Type I error
        beta: Probability of committing Type II error
        sides: Number of sides for the test (i.e. if we want to conclude
            that a negative result is not within the hull hypothesis distribution)
        delta: the minimum detectable effect of the test, given 
            everything else
        variance: The variance of the underyling outcome
    '''
    def __init__(self, alpha, beta, sides):
        self.alpha = alpha,
        self.beta = beta,
        self.sides = sides

    def get_sample_size(self, variance, delta):
        n = 2*(stats.norm.ppf(self.alpha/self.sides) + stats.norm.ppf(self.beta))**2 *((np.sqrt(variance)/delta)**2)
        return(n)