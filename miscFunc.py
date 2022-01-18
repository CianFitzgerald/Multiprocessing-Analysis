import time
import math
import multiprocessing
from multiprocessing import Pool


# A function for timing a job that uses a pool of processes.
#  f is a function that takes a single argument
#  data is an array of arguments on which f will be mapped
#  pool_size is the number of processes in the pool. 
def pool_process(f, data, pool_size):
    tp1 = time.time()
    pool = Pool(processes=pool_size) # initialize the Pool.
    result = pool.map(f, data)       # map f to the data using the Pool of processes to do the work 
    pool.close() # No more processes
    pool.join()  # Wait for the pool processing to complete. 
    return int(time.time()-tp1)

    
def check_prime(num):
    t1 = time.time()
    res = False
    if num > 0:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                print("Time:", int(time.time()-t1))
                break
        else:
            print(num,"is a prime number")
            print("Time:", time.time()-t1) 
            res = True
            # if input number is less than
            # or equal to 1, it is not prime
    return res


def Iterative_factorial(n):
    t1 = time.time()
    #return an error message if the number inputeed is less than 0.
    if n<0:
        return "error: factorials cannot be defined for negative numbers"
    
    #initialize the result to 1
    result = 1
    
    #for loop iterating over all numbers from 2 up to n+1
    #by beginning the loop at 2 we ensure that 0 and 1 return a result of 1.
    for i in range(2, n+1): 
        
        #assign the product of result with i to the variable result 
        result *= i 
        
    #Return the final result 
    print("Time:", time.time()-t1) 
    return result 



