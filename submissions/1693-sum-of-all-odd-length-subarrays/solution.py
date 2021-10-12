class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ret = sum(arr)
        for i in range(3, len(arr) + 1, 2):
            for j in range(0, len(arr) - i + 1):
                ret += sum(arr[j:j + i])
        
        return ret
