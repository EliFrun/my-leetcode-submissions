class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        n = [2 ** i for i, x in enumerate(list(bin(n)[2:][::-1])) if x == '1']

        pre = [1]
        for v in n:
            pre.append(v * pre[-1])

        
        return [pre[r + 1] // pre[l] % 1_000_000_007 for l,r in queries]
        
