class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0
        
        primes = [1] * n
        primes[0] = primes[1] = 0
        for i in range(2, round(n**0.5) + 1):
            if primes[i]:
                primes[i*i: n: i] = [0] * ((n-1 - i*i) // i + 1)
                # n = 11
                # i = 2
                # (n-1-i*i)//i + 1
                # (n-1)               # get total # of indicies for n (non-inclusive)
                #     -i*i            # shift to get # of slots in range of interest
                #          //i        # get number of groups
                #              + 1    # get number of slots
                # strikes[2*2:11:2]  = [0] * ((11-1-2*2)//2 + 1
                # strikes[4:11:2]    = [0] * 4
                # s[4], s[6], s[8], s10] = 0, 0, 0, 0
        return sum(primes)