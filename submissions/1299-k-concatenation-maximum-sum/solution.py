class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if k == 0:
            return 0

        best_subarray = -100000000  # or: float('-inf')
        best_start = best_end = 0  # or: None
        current_sum = 0
        for current_end, x in enumerate(arr):
            if current_sum <= 0:
                current_start = current_end
                current_sum = x
            else:
                current_sum += x
            if current_sum > best_subarray:
                best_subarray = current_sum
                best_start = current_start
                best_end = current_end + 1
                
        if k == 1:
            return max(best_subarray, 0)

        best_sum_left = 0
        curr = 0
        for v in arr:
            curr += v
            best_sum_left = max(best_sum_left, curr)

        best_sum_right = 0
        curr = 0
        for v in arr[::-1]:
            curr += v
            best_sum_right = max(best_sum_right, curr)
       
        val = sum(arr) * (k - 2)
        if best_sum_left > 0:
            val += best_sum_left

        if best_sum_right > 0:
            val += best_sum_right

        if val < 0:
            return max(0, best_sum_left + best_sum_right, best_subarray)

        return max(0, best_subarray, best_sum_right + best_sum_left, val) % (1_000_000_007)
