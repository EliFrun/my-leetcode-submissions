class Solution:
    def reinitializePermutation(self, p: int) -> int:
        curr = 1
        visited = set()
        n = 0
        while curr not in visited:
            visited.add(curr)
            n += 1
            if curr % 2 == 0:
                curr = curr // 2
            else:
                curr = p // 2 + (curr - 1) // 2
        return n

            
