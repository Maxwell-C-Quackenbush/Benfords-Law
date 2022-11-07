import math
import numpy as np

# gets the n-th digit of a given number. 
# e.g. returns 3 for: 3456.78, 1
#      returns 5 for: 3456.78, 3
# if the requested digit is larger than the number
# e.g. requesting the 2nd digit of 5, the function returns NaN
def get_digit(number, nth=1):
    order = math.floor( math.log10(number) );

    if (nth > order):
        return math.nan

    num_str = str(number);
    return int( num_str[nth-1] )

# Extract the distribution associated
def benfor_distribution():
    Pd = []
    for i in range(9):
        Pd[i] = math.log10(1 + 1/(i+1))
    return Pd



def test_gaussian():
    # Generate 1000 Gaussian distributed points (around 0 with normal distribution of 10) 
    X = np.random.normal(0,10,1000)
    dist = np.array(9)

    for i in range(len(X)):
        dig = get_digit(X[i])
        dist[dig] += 1

    return dist / len(X)






