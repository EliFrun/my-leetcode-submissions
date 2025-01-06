class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1

        for k in counter.keys():
            counter[k] = min(counter[k], 3)
        
        nums = []
        for k,v in counter.items():
            nums += [k] * v

        ret = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                x = nums[i]
                y = nums[j]
                target = - (x + y)
                if counter[target] == 0:
                    continue
                
                counts = defaultdict(int)
                counts[x] += 1
                counts[y] += 1
                counts[target] += 1
                res = []
                for k,v in counts.items():
                    res.append(counter[k] - v)

                if all([a >= 0 for a in res]):
                    ret.add(
                        tuple(
                            sorted(
                                [x, y, target]
                            )
                        )
                    )

        return list(ret)
                

        
