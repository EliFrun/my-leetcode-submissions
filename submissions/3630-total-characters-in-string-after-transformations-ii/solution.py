class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 1_000_000_007
        def matrix_add(m1, m2):
            ret = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for j in range(26):
                    ret[i][j] = (m1[i][j] + m2[i][j]) % mod
            return ret
        
        def matrix_multiply(m1, m2):
            ret = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for j in range(26):
                    ret[i][j] = sum(m1[i][k] * m2[k][j] for k in range(26)) % mod
            return ret

        def matrix_power(m1, exp):
            ret = [[1 if i == j else 0 for i in range(26)] for j in range(26)]
            while exp > 0:
                if exp & 1:
                    ret = matrix_multiply(ret, m1)
                m1 = matrix_multiply(m1, m1)
                exp >>= 1
            return ret

                        
        m = []
        for i, num in enumerate(nums):
            l = [0] * 26
            for j in range(1, num + 1):
                l[(i + j) % 26] = 1
            m.append(l)


        c = Counter(s)
        counts = [[0] * 26 for _ in range(26)]
        for k,v in c.items():
            counts[ord(k) - ord('a')][ord(k) - ord('a')] = v

        
        res = matrix_multiply(counts, matrix_power(m, t))
        return sum(sum(x) for x in res) % mod

            
        
