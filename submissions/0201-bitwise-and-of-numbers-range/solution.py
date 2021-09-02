class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0:
            return 0
        if left == right:
            return left
        return left & right & ~(2 ** int(log(right - left, 2) + 1) - 1)
