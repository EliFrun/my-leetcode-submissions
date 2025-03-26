class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def is_sorted(i):
            for j in range(len(strs) - 1):
                if strs[j][i] > strs[j + 1][i]:
                    return False
            return True

        return len([i for i in range(len(strs[0])) if not is_sorted(i)])

