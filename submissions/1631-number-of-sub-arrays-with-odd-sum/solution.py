class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix = [0]
        for n in arr:
            prefix.append(prefix[-1] + n)

        ret = 0
        evens = 0
        odds = 0
        for n in prefix:
            if n & 1 == 0:
                evens += 1
                ret += odds
            else:
                odds += 1
                ret += evens

        return ret % 1_000_000_007
