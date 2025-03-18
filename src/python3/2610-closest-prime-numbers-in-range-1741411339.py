class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime_num = [True] * (right + 1)
        is_prime_num[0] = is_prime_num[1] = False

        for i in range(2, int(right**0.5) + 1):
            if is_prime_num[i]:
                for j in range(i*i, right + 1, i):
                    is_prime_num[j] = False
        
        primes = [i for i in range(left, right + 1) if is_prime_num[i]]
        
        if len(primes) < 2:
            return [-1, -1]
        else:
            diff = float('inf')
            closest_primes = []
            
            for i in range(1, len(primes)):
                curr_diff = primes[i] - primes[i-1]
                if curr_diff < diff:
                    diff = curr_diff
                    closest_primes = [primes[i-1], primes[i]]
            
            return closest_primes
