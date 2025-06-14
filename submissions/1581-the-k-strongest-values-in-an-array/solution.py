class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        m = sorted(arr)[(len(arr) - 1)//2]
        arr.sort(key=lambda x: (abs(x - m), x))
        return arr[len(arr) - k:]
