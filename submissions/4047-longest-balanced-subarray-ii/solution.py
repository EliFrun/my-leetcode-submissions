class SegTree:
    def __init__(self, left, right):
        self.modifier = 0
        self.left_n = None
        self.right_n = None
        self.left = left
        self.right = right
        self.idx = left
        self.min = 0
        self.max = 0
        if left != right:
            middle = (left + right) // 2
            self.left_n = SegTree(left, middle)
            self.right_n = SegTree(middle + 1, right)

    def update(self, left, right, m):
        if left <= self.left and self.right <= right:
            self.modifier += m
            self.min += m
            self.max += m
            return (self.min, self.max)
        if self.right < left:
            return (self.min, self.max)
        if self.left > right:
            return (self.min, self.max)
        if self.left_n:
            left_min, left_max = self.left_n.update(left,right,m)
        if self.right_n:
            right_min, right_max = self.right_n.update(left,right,m)

        self.min = min(left_min, right_min) + self.modifier
        self.max = max(left_max, right_max) + self.modifier
        return (self.min, self.max)

    def find_zero(self, modification, left, right):
        if self.right < left:
            return float('inf')
        if self.left > right:
            return float('inf')
        if modification + self.min > 0:
            return float('inf')
        if modification + self.max < 0:
            return float('inf')
        
        if not self.left_n and not self.right_n:
            if self.modifier + modification == 0:
                return self.idx
            else:
                return float('inf')
        
        if self.left_n:
            if (v := self.left_n.find_zero(modification + self.modifier, left, right)) != float('inf'):
                return v
        if self.right_n:
            if (v:= self.right_n.find_zero(modification + self.modifier, left, right)) != float('inf'):
                return v
        return float('inf')

    def nav(self, modification):
        if not self.left_n and not self.right_n:
            print(f'{self.left}:{modification + self.modifier}', end=' ')
        else:
            self.left_n.nav(modification + self.modifier)
            self.right_n.nav(modification + self.modifier)

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        s = SegTree(0, len(nums) - 1)
        d = defaultdict(lambda: -1)

        ret = 0
        for i, num in enumerate(nums):
            s.update(d[num] + 1, i, -1 if num & 1 else 1)
            idx = s.find_zero(0, 0, i)
            ret = max(ret, i - idx + 1)
            d[num] = i

        return ret

        
        
