class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        balls_left = 0
        balls_right = boxes.count('1')
        left_sum = 0
        right_sum = sum([i for i,v in enumerate(boxes) if v == '1'])
        ret = []
        for c in boxes:
            balls_right -= 1 if c == '1' else 0
            ret.append(right_sum + left_sum)
            balls_left += 1 if c == '1' else 0
            left_sum += balls_left
            right_sum -= balls_right

        return ret


        
