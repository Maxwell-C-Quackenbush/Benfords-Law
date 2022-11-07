import math
import numpy as np
import matplotlib.pyplot as plt


# gets the n-th digit of a given number. 
# e.g. returns 3 for: 3456.78, 1
#      returns 5 for: 3456.78, 3
# if the requested digit is larger than the number
# e.g. requesting the 2nd digit of 5, the function returns NaN
def get_digit(number, nth=1):
    number = np.abs(number)
    
    if number < 1:
        return 0
    order = math.floor( math.log10(number) );

    if (nth > order):
        return 0

    num_str = str(number);
    return int( num_str[nth-1] )

# Extract the distribution associated
def benfor_distribution():
    Pd = np.zeros(9)
    for i in range(9):
        Pd[i] = math.log10(1 + 1/(i+1))
    return Pd



def test_gaussian():
    # Generate 1000 Gaussian distributed points (around 0 with normal distribution of 10) 
    X = np.random.normal(0,1000,1000)
    dist = np.zeros(10)

    for i in range(len(X)):
        dig = get_digit(X[i])
        dist[dig] += 1

    return dist[1:10] / (len(X)-dist[0])




def main():
    
    benford_dist = benfor_distribution()
    gaussian_dist = test_gaussian()
    
    idx = np.arange(1,10)
    
    plt.rc('lines', linewidth=2.5)
    fig, ax = plt.subplots()
    
    ax.plot(idx, benford_dist, label="Benford distribution")
    ax.plot(idx, gaussian_dist, label="Gaussian distribution")
    
    ax.legend(handlelength=2)
    plt.show()
    
    
    
    
    
    
if __name__ == "__main__":
    main()



