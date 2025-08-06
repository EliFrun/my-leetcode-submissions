class SegTree:
    def __init__(self, lis):
        self.idx = float('inf')
        self.min = float('inf')
        self.max = 0
        self.left = None
        self.right = None
        
        if len(lis) == 1:
            self.min = lis[0][0]
            self.max = lis[0][0]
            self.idx = lis[0][1]
        else:
            left, right = lis[:len(lis)//2], lis[len(lis)//2:]
            if left:
                self.left = SegTree(left)
                self.min = min(self.min, self.left.min)
                self.max = max(self.max, self.left.max)
                self.idx = min(self.idx, self.left.idx)
            if right:
                self.right = SegTree(right)
                self.min = min(self.min, self.right.min)
                self.max = max(self.max, self.right.max)
                self.idx = min(self.idx, self.right.idx)

    def __str__(self):
        if not self.left and not self.right:
            return str(self.idx)
        return self.left.__str__() + ',' + self.right.__str__()

    def find(self, val):
        ret = float('inf')
        if val > self.max:
            return ret
        if val <= self.min:
            return self.idx
        if self.left:
            ret = min(ret, self.left.find(val))
        if self.right:
            ret = min(ret, self.right.find(val))
        return ret

    def remove(self, val, idx):
        if not self.min <= val <= self.max:
            return
        if self.idx > idx:
            return
        if not self.left and not self.right:
            if self.idx == idx:
                self.idx = float('inf')
                self.min = float('inf')
                self.max = 0
            return
        if self.left:
            self.left.remove(val, idx)
        if self.right:
            self.right.remove(val, idx)
        self.idx = min(self.left.idx, self.right.idx)
        self.min = min(self.left.min, self.right.min)
        self.max = max(self.left.max, self.right.max)
        

        

            

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        st = SegTree(sorted([(x,i) for i,x in enumerate(baskets)]))
        ret = 0
        for fruit in fruits:
            idx = st.find(fruit)
            if idx == float('inf'):
                ret += 1
            else:
                st.remove(baskets[idx], idx)
        return ret
        

        
