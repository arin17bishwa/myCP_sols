class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even_cnt = 5
        prime_cnt = 4
        ans = 1
        mod = 10**9 + 7
        odd_places = n >> 1
        even_places = n - odd_places
        return (pow(even_cnt, even_places, mod) * pow(prime_cnt, odd_places, mod)) % mod
