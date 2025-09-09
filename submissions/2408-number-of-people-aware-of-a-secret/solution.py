class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # [people who know, people who can tell, people who will forget]
        curr = [0] * forget
        curr[0] = 1
        print(curr)
        for i in range(n - 1):
            nxt = [0] + curr[:-1]
            for j in range(delay - 1, forget - 1):
                nxt[0] += curr[j]

            curr = nxt
        return sum(curr) % (1_000_000_007)

