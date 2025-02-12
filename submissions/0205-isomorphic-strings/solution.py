class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def seq(st):
            i = 0
            nums = {
                st[0]: i
            }
            ret = [0]
            for c in st[1:]:
                if c in nums:
                    ret.append(nums[c])
                else:
                    i += 1
                    nums[c] = i
                    ret.append(i)

            return ret

        return all([x == y for x,y in zip(seq(s), seq(t))])
        
