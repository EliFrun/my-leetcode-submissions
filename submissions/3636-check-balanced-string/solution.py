class Solution:
    def isBalanced(self, num: str) -> bool:
        odds = 0
        evens = 0
        for i, v in enumerate(num):
            if i % 2 == 0:
                evens += int(v)
            else:
                odds += int(v)

        return odds == evens
        
