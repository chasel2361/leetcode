class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        
        cnt = 0
        for n_ptr in range(2, n):
            ptr_basis = round(n_ptr**0.5)
            is_prime = True
            for i in range(2, ptr_basis + 1):
                if n_ptr % i == 0:
                    is_prime = False
                    break
            if is_prime:
                cnt += 1
        return cnt