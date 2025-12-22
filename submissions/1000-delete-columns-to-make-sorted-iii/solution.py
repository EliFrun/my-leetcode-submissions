class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        @cache
        def solve(idx):
            if idx >= len(strs[0]):
                return 0
            
            ret = len(strs[0]) - idx - 1
            for i in range(idx + 1, len(strs[0])):
                if all(st[i] >= st[idx] for st in strs):
                    ret = min(ret, i - idx - 1 + solve(i))
                
            return ret

        return min([i + solve(i) for i in range(len(strs[0]))])
