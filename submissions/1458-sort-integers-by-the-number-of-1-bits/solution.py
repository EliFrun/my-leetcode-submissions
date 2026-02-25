class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: ([sum(((x >> y) & 1 for y in range(32)))], x))
