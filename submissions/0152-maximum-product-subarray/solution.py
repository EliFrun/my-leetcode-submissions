class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lists = []
        curr = []
        zero_exists = False
        for n in nums:
            if n == 0:
                if len(curr) > 0:
                    lists.append(curr)
                    curr = []
                zero_exists = True
                continue

            curr.append(n)
        
        if len(curr) > 0:
            lists.append(curr)

        def solve(lis):
            if len(lis) == 1:
                return lis[0]
            count_negatives = len([x for x in lis if x < 0])
            if count_negatives % 2 == 0:
                ret = 1
                for n in lis:
                    ret *= n
                return ret

            else:
                negative_idxs = [i for i,v in enumerate(lis) if v < 0]
                first_idx = negative_idxs[0]
                last_idx = negative_idxs[-1]
                pos1 = 1
                for n in lis[:first_idx]:
                    pos1 *= n

                pos2 = 1
                for n in lis[first_idx + 1:]:
                    pos2 *= n

                pos3 = 1
                for n in lis[:last_idx]:
                    pos3 *= n

                pos4 = 1
                for n in lis[last_idx + 1:]:
                    pos4 *= n

                return max(pos1, pos2, pos3, pos4)
        return max(
            [solve(lis) for lis in lists] + ([0] if zero_exists else [])
        )

                
        
