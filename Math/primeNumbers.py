class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        primes=[1]*A
        primes.append(1)
        primes[0]=0
        primes[1]=0
        import math
        root_A=int(math.sqrt(A))
        for i in range(2,root_A+1):
            if primes[i]==1:
                j=2
                while i*j<= A:
                    primes[i*j]=0
                    j+=1
        myList=[]
        for i in range(0,len(primes)):
            if primes[i]==1:
                myList.append(i)
        return myList
            
        

