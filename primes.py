import time
primes = [2]
n = int(input("Enter the upper range for which to find primes for"))
tic = time.perf_counter()
counter=0
for x in range(3, n+1):
    for y in range(0, len(primes)-1):
        if(x%primes[y]==0):
            counter=counter+1
    if counter==0:
        primes.append(x)
        #print(x, end = " ")
        counter=0
    else:
        counter=0
toc = time.perf_counter()
print(primes)
print("Calculated in",(toc - tic), "seconds")
    
        

