class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        holders = [0] * n

        found = False
        curr = 0
        iteration = 1
        while not found:
            holders[curr] += 1
            if holders[curr] == 2:
                found = True
            curr = (curr + iteration * k) % n
            iteration += 1

        return [i + 1 for i, v in enumerate(holders) if v == 0]
        
