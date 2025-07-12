class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @cache
        def solve(nums):
            if not nums:
                return (1,1)
            nums = list(nums)
            mi, ma = float('inf'), 0
            for i in range(0, pow(2, len(nums)//2)):
                next_list = []
                for l, r in zip(nums[:len(nums)//2 + 1], nums[len(nums) - 1:len(nums)//2 - 1:-1]):
                    if l == firstPlayer and r == secondPlayer:
                        return (1,1)
                    elif l in (firstPlayer, secondPlayer):
                        next_list.append(l)
                    elif r in (firstPlayer, secondPlayer):
                        next_list.append(r)
                    else:
                        next_list.append(r if i & 1 else l)
                    i >>= 1
                mmi, mma = solve(tuple(sorted(next_list)))
                mi = min(mi, 1 + mmi)
                ma = max(ma, 1 + mma)
            return (mi, ma)

        return solve(tuple(list(range(1, n + 1))))
                    
