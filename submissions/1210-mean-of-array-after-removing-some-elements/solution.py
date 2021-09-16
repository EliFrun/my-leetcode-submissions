class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        return sum(arr[len(arr)//20:len(arr)- len(arr)//20]) / (.9 * len(arr))
