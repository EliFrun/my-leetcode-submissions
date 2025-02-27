class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        valid = set(arr)

        ret = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] in valid:
                    m = arr[i]
                    n = arr[j]
                    seq = 2
                    while m + n in valid:
                        m, n = (n, m + n)
                        seq += 1

                    if seq > 2:
                        ret = max(ret, seq)

        return ret
        
