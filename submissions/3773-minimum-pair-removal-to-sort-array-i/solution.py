class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        q = SortedList()
        bad_pairs = set()
        indexes = SortedList(range(len(nums)))
        for i in range(len(nums) - 1):
            q.add((nums[i] + nums[i + 1], i, i + 1))
            if nums[i] > nums[i + 1]:
                bad_pairs.add((i, i + 1))

        ret = 0
        while bad_pairs:
            #print(ret, q, indexes, bad_pairs, nums)
            v, i, j = q.pop(0)
            ret += 1
            if (i, j) in bad_pairs:
                bad_pairs.remove((i, j))

            idx_i = indexes.bisect_left(i)
            idx_j = indexes.bisect_left(j)
            # left_pair logic
            if idx_i > 0:
                l, r = indexes[idx_i - 1], indexes[idx_i]
                q.remove((nums[l] + nums[r], l, r))
                if (l,r) in bad_pairs:
                    bad_pairs.remove((l,r))
                q.add((nums[l] + v, l, r))
                if nums[l] > v:
                    bad_pairs.add((l, r))
            
            # right pair logic
            if idx_j < len(indexes) - 1:
                l, r = indexes[idx_j], indexes[idx_j + 1]
                q.remove((nums[l] + nums[r], l, r))
                if (l,r) in bad_pairs:
                    bad_pairs.remove((l,r))
                q.add((nums[r] + v, indexes[idx_i], r))
                if v > nums[r]:
                    bad_pairs.add((indexes[idx_i], r))
            
            indexes.pop(idx_j)
            nums[indexes[idx_i]] = v

        return ret
            
            


            

            
            
            

        
