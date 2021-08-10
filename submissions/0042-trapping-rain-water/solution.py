class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) <= 2:
            return 0

        current, lookforward = 0, 1
        ret = 0
        
        while current < len(height):
            if height[current] == 0:
                current += 1
                lookforward = current + 1
                continue
                
            second_highest = 0
            second_highest_index = current + 1
            while lookforward < len(height) and height[lookforward] < height[current]:
                if height[lookforward] >= second_highest:
                    second_highest = height[lookforward] 
                    second_highest_index = lookforward
                lookforward += 1
                
            if lookforward >= len(height):
                lookforward = second_highest_index
                current_height = second_highest
            else:
                 current_height = height[current]

            while current < lookforward:
                    ret += max(0, current_height - height[current])
                    current += 1

            lookforward = current + 1
                
        return ret
