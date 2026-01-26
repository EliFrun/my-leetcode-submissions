class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        m = min(arr[i + 1] - arr[i] for i in range(len(arr) - 1))
        ret = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == m:
                ret.append([arr[i], arr[i + 1]])

        return ret
        
