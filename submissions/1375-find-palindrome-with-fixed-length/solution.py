class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        def solve(v):
            v = str(10 ** ((intLength - 1)//2) + v - 1)
            if 2 * len(v) - (1 if intLength & 1 else 0) > intLength:
                return -1
            if intLength & 1:
                return int(v + v[:len(v) - 1][::-1])
            return int(v + v[::-1])

        return [solve(x) for x in queries]
        
