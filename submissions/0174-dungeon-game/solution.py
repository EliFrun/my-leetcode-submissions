class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        memo = [[-1 for _ in dungeon[0]] for __ in dungeon]
        memo[-1][-1] = max(0,-dungeon[-1][-1])

        curr = [(len(dungeon) - 2, len(dungeon[0]) - 1),(len(dungeon) - 1, len(dungeon[0]) - 2)]
        while curr:
            nxt = set()
            for i,j in curr:
                if i < 0:
                    continue
                if j < 0:
                    continue
                for di, dj in [(-1,0), (0,-1)]:
                    nxt.add((i + di, j + dj))
                    below = memo[i + 1][j] if i + 1 < len(dungeon) else 1_000_000
                    right = memo[i][j + 1] if j + 1 < len(dungeon[0]) else 1_000_000
                    memo[i][j] = max(0, min(below, right) - dungeon[i][j])

            curr = nxt

        return memo[0][0] + 1

        
