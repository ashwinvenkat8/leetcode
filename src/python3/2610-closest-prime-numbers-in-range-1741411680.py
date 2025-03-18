class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(n: int) -> bool:
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            
            i = 5

            while i*i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        primes = []

        for n in range(max(2, left), right + 1):
            if is_prime(n):
                primes.append(n)
        
        if len(primes) < 2:
            return [-1, -1]
        
        diff = float('inf')
        closest_primes = []

        for i in range(1, len(primes)):
            curr_diff = primes[i] - primes[i-1]

            if curr_diff < diff:
                diff = curr_diff
                closest_primes = [primes[i-1], primes[i]]
        
        return closest_primes
