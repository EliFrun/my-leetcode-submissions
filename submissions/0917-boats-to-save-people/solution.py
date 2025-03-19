class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ret = 0
        left = 0; right = len(people) - 1
        while left <= right:
            if people[right] >= limit:
                right -= 1
            elif people[right] + people[left] > limit:
                right -= 1
            else:
                right -= 1
                left += 1
            
            ret += 1

        return ret
        
