class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        arrs = []
        curr = []
        for num in nums:
            if num != 0:
                curr.append(num//abs(num))
            else:
                if curr:
                    arrs.append(curr)
                    curr = []
        if curr:
            arrs.append(curr)


        ret = 0
        for arr in arrs:
            r = prod(arr)
            if r > 0:
                ret = max(ret, len(arr))
            else:
                idx = arr.index(-1)
                l_idx = idx
                for i in range(len(arr) - 1, -1, -1):
                    if arr[i] == -1:
                        l_idx = i
                        break

                ret = max(ret, idx, len(arr) - 1 - l_idx, l_idx, len(arr) - 1 - idx, l_idx - idx)
        return ret

        
