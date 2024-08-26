class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [combo for combo in itertools.combinations(list(range(1,10)), k) if sum(combo) == n]

         

