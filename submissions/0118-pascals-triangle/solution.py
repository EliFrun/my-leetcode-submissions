class Solution:
    def generate(self, r: int) -> List[List[int]]:
        ret = [[1]]
        curr = [1] * min(r, 2)
        for _ in range(r - 1):
            ret.append(curr)
            nxt = [1]
            for i in range(len(curr) - 1):
                nxt.append(curr[i] + curr[i + 1])
            nxt.append(1)
            curr = nxt

        return ret
        
