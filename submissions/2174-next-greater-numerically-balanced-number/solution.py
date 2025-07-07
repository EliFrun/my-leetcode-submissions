class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        if n == 0:
            return 1
        p = int(log10(n)) + 1

        ret_seq = {
            1: [22],
            2: [122],
            3: [1333],
            4: [14444],
            5: [122333],
            6: [1224444],
            7: [1224444]
        }

        m = {
            1: [],
            2: [(2,)],
            3: [(1,2), (3,)],
            4: [(1,3), (4,)],
            5: [(1,4), (2,3), (5,)],
            6: [(1,2,3), (1,5), (2,4), (6,)],
            7: []
        }

        nums = []
        for lis in m[p]:
            s = ""
            for v in lis:
                s += str(v) * v
            nums.extend([int(''.join(x)) for x in permutations(s)])

        nums += ret_seq[p]

        for num in sorted(nums):
            if n < num:
                return num



        
