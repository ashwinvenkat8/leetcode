class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left >= right or right < 2:
            return [-1, -1]
        
        is_prime_num = [True] * (right - left + 1)

        if left == 0:
            is_prime_num[0] = is_prime_num[1] = False
        elif left == 1:
            is_prime_num[0] = False

        for i in range(2, int(right**0.5) + 1):
            first_multiple = max((i * i), (left + (i - left % i) % i))
            
            for multiple in range(first_multiple, right + 1, i):
                is_prime_num[multiple - left] = False
        
        primes = [left+i for i, is_prime in enumerate(is_prime_num) if is_prime]
        
        if len(primes) < 2:
            return [-1, -1]
        else:
            diff = float('inf')
            closest_primes = []
            l, r = 0, 1
            
            while r < len(primes):
                if (primes[r] - primes[l]) < diff:
                    diff = primes[r] - primes[l]
                    closest_primes = [primes[l], primes[r]]
                l += 1
                r += 1
            
            return closest_primes
