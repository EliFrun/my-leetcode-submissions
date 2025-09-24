class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x for x,y in sorted(Counter(nums).items(), reverse=True, key=lambda x: x[1])][:k]
        
        
