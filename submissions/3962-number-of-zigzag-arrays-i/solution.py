MOD = 10**9 + 7
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        k = r - l + 1

        dp_up = [1] * k
        dp_down = [1] * k

        psum_up = [0] * (k + 1)
        psum_down = [0] * (k + 1)
        for i in range(k):
            psum_up[i + 1] = (psum_up[i] + dp_up[i]) % MOD
            psum_down[i + 1] = (psum_down[i] + dp_down[i]) % MOD

        for j in range(2, n + 1):
            new_dp_up = [0] * k
            new_dp_down = [0] * k
            new_psum_up = [0] * (k + 1)
            new_psum_down = [0] * (k + 1)
            for i in range(k):
                if i > 0:
                    new_dp_up[i] = psum_down[i]  % MOD 
                new_dp_down[i] = (psum_up[k] - psum_up[i + 1]) % MOD 

                new_psum_up[i + 1] = (new_psum_up[i] + new_dp_up[i]) % MOD
                new_psum_down[i + 1] = (new_psum_down[i] + new_dp_down[i]) % MOD

            dp_up, dp_down = new_dp_up, new_dp_down
            psum_up, psum_down = new_psum_up, new_psum_down

        return (sum(dp_up) + sum(dp_down)) % MOD
        
