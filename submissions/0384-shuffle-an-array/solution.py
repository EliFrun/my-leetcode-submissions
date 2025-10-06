class Solution:

    def __init__(self, nums: List[int]):
        self.og_lis = nums
        self.curr_lis = deepcopy(nums)
        

    def reset(self) -> List[int]:
        return self.og_lis
        

    def shuffle(self) -> List[int]:
        i, j = randint(0, len(self.curr_lis) - 1), randint(0, len(self.curr_lis) - 1)
        self.curr_lis[i], self.curr_lis[j] = self.curr_lis[j], self.curr_lis[i]
        return self.curr_lis
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
