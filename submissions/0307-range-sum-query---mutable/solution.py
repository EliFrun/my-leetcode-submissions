class SegTree:

    def __init__(self, left, right, lis):
        self.sum = lis[left]
        self.left = left
        self.right = right
        self.left_n = None
        self.right_n = None
        if left != right:
            self.left_n = SegTree(left, left + (right - left) // 2, lis)
            self.right_n = SegTree(left + (right - left) // 2 + 1, right, lis)
            self.sum = self.left_n.sum + self.right_n.sum

    def update(self, idx, val):
        if self.left > idx:
            return
        if self.right < idx:
            return
        
        if self.left == self.right and self.left == idx:
            self.sum = val
            return

        self.left_n.update(idx, val)
        self.right_n.update(idx, val)
        self.sum = self.left_n.sum + self.right_n.sum

    def find(self, left, right):
        if self.right < left:
            return 0
        if self.left > right:
            return 0

        if left <= self.left and self.right <= right:
            return self.sum

        return self.left_n.find(left, right) + self.right_n.find(left, right)

class NumArray:

    def __init__(self, nums: List[int]):
        self.s = SegTree(0, len(nums) - 1, nums)
        

    def update(self, index: int, val: int) -> None:
        self.s.update(index, val)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.s.find(left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
