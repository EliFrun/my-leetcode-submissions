class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        counts = defaultdict(int)
        for i in range(len(nums) - 1):
            if nums[i] == key:
                counts[nums[i + 1]] += 1
            
        return sorted(list(counts.items()), key=lambda x: -x[1])[0][0]
        
