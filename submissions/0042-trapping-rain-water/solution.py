class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ret = 0
        while l < r:
            if height[l] <= height[r]:
                ret += max(0, height[l] - height[l + 1])
                height[l + 1] = max(height[l], height[l + 1])
                l += 1
            else:
                ret += max(0, height[r] - height[r - 1])
                height[r - 1] = max(height[r], height[r - 1])
                r -= 1

        return ret

