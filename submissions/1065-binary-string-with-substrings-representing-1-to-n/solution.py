class Solution:
    def queryString(self, s: str, n: int) -> bool:
        curr = []
        nums = set()
        for c in s:
            if len(curr) > log2(n):
                curr.pop(0)
            curr.append(c)
            for i in range(len(curr)):
                nums.add(int(''.join(curr[i:]), 2))
    
        for i in range(1, n + 1):
            if i not in nums:
                return False
        return True

        
