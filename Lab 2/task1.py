
def factorial(n):
    if(n==0):
        return 1
    else:
        return n* factorial(n-1)
    
import time
start_time = time.time()
n = 1500
ans= factorial(n)
end_time = time.time()
runtime = end_time - start_time
print("Runtime of factorial at",n,"is",runtime,"seconds")


#Problem 1
print("Problem 1:" + "\n")
import numpy as np

def RandomArray(size):
    rand_array = np.random.randint(-200,200,size)
    return rand_array

print(RandomArray(20))
