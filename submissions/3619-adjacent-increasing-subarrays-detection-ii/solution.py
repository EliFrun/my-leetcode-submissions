class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        lists = []
        curr = []
        for num in nums:
            if curr == []:
                curr = [num]
            elif curr[-1] >= num:
                lists.append(curr)
                curr = [num]
            else:
                curr.append(num)
        lists.append(curr)   

        print(lists) 

        longest = len(lists[0]) // 2
        for i in range(len(lists) - 1):
            longest = max(
                longest,
                len(lists[i]) // 2,
                len(lists[i + 1]) // 2,
                min(
                    len(lists[i]),
                    len(lists[i + 1])
                )
            )

        return longest
