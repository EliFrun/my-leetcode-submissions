class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        ret = 0
        
        idx = bisect_left(fruits, [startPos, float('inf')])
        left, right = fruits[:idx], fruits[idx:]

        left_idx = 0
        left_sum = sum([v for p,v in left] + [0])
        right_sum = 0
        for pos, val in right:
            if pos > startPos + k:
                break
            right_sum += val
            new_k = max(0, k - pos + startPos)
            while left and left_idx < len(left) and left[left_idx][0] < pos - new_k:
                left_sum -= left[left_idx][1]
                left_idx += 1

            ret = max(ret, left_sum + right_sum)

        idx = bisect_left(fruits, [startPos, float('inf')])
        left, right = fruits[:idx], fruits[idx:]

        right_idx = len(right) - 1
        left_sum = 0
        right_sum = sum([v for p,v in right] + [0])
        for pos, val in left[::-1]:
            if startPos - k > pos:
                break
            left_sum += val
            new_k = max(0, k - startPos + pos)
            while right and right_idx >= 0 and right[right_idx][0] > pos + new_k:
                right_sum -= right[right_idx][1]
                right_idx -= 1

            ret = max(ret, left_sum + right_sum)

        return ret


            

        
