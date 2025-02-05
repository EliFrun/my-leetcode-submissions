class Solution:
    def minSteps(self, n: int) -> int:
        facts = []
        for i in range(2, n + 1):
            while n % i == 0:
                facts.append(i)
                n = n // i
            if n == 1:
                break

        
        return sum(facts)
        
