class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        triple = [nums[0]]
        for num in nums:
            for i in range(len(triple)):
                if num < triple[i]:
                    triple[i] = num
                    break
                if num == triple[i]:
                    break
                if num > triple[-1]:
                    triple.append(num)
                if len(triple) > 2:
                    return True
        return False

        
