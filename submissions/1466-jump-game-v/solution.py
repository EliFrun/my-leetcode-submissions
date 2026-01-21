class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        g = defaultdict(list)
        for i in range(len(arr)):
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[i] > arr[j]:
                    g[i].append(j)
                else:
                    break

            for j in range(i + 1, min(i + d + 1, len(arr))):
                if arr[i] > arr[j]:
                    g[i].append(j)
                else:
                    break
        

        @cache
        def dfs(idx):
            ret = 0
            for v in g[idx]:
                ret = max(ret, dfs(v))

            return 1 + ret

        return max(dfs(x) for x in range(len(arr)))
