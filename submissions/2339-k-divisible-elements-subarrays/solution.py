class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        unique = set()
        c = 0
        left = 0
        ret = 0
        for i in range(len(nums)):
            c += 1 if nums[i] % p == 0 else 0
            while c > k:
                c -= 1 if nums[left] % p == 0 else 0
                left += 1
            
            for j in range(left, i + 1):
                unique.add(tuple(nums[j:i + 1]))


        return len(unique)

        
