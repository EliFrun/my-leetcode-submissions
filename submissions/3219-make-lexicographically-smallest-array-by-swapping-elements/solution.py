class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], k: int) -> List[int]:
        tmp = sorted(list(enumerate(nums)), key=lambda x: x[1])
        blocks = []
        curr = [tmp[0]]

        for i, v in tmp[1:]:
            if v <= curr[-1][1] + k:
                curr.append((i, v))
            else:
                blocks.append(curr)
                curr = [(i, v)]

        blocks.append(curr)

        ret = [0] * len(nums)
        for b in blocks:
            values = [v for i,v in b]
            indexes = sorted([i for i,v in b])

            for i, v in zip(indexes, values):
                ret[i] = v

        return ret
