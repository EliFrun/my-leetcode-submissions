class Node:

    def __init__(self, idx, val, left=None, right=None):
        self.idx = idx
        self.val = val
        self.left = left
        if self.left:
            self.left.right = self
        self.right = right

    def pop_self(self):
        if self.left:
            self.left.right = self.right
        if self.right:
            self.right.left = self.left

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        sums = {}
        bad_indexes = set()
        q = SortedList()
        head = Node(-1, -1)
        curr = head
        for i, num in enumerate(nums):
            n = Node(i, num, curr)
            if i < len(nums) - 1:
                if num > nums[i + 1]:
                    bad_indexes.add(i)
                sums[i] = num + nums[i + 1]
                q.add((num + nums[i + 1], i, n))
            curr = n
        head = head.right
        head.left = None

        def print_state():
            print(q, bad_indexes)
            curr = head
            while curr:
                print(curr.val, curr.idx, end=' ')
                curr = curr.right
            print()
        
        cnt = 0
        while bad_indexes:
            #print_state()
            
            s, idx, node = q.pop(0)

            right = node.right
            if right.idx in bad_indexes:
                bad_indexes.remove(right.idx)
            if right.idx in sums:
                q.remove((sums[right.idx], right.idx, right))
                sums.pop(right.idx)
            right.pop_self()

            if idx in bad_indexes:
                bad_indexes.remove(node.idx)

            node.val = s
            right = node.right
            if right:
                s = node.val + right.val
                sums[idx] = s
                if node.val > right.val:
                    bad_indexes.add(node.idx)
                q.add((sums[idx], idx, node))
            else:
                sums.pop(idx)
            
            left = node.left
            if left:
                q.remove((sums[left.idx], left.idx, left))
                sums[left.idx] = left.val + node.val
                q.add((sums[left.idx], left.idx, left))
                if left.val > node.val:
                    bad_indexes.add(left.idx)
                else:
                    if left.idx in bad_indexes:
                        bad_indexes.remove(left.idx)


            cnt += 1
        return cnt




            
            


            

            
            
            

        
