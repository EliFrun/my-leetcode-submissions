class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def dist(curr, targ):
            return abs(curr[0] - targ[0]) + abs(curr[1] - targ[1])

        d = dist((0,0), target)
        return all([d < dist(target, x) for x in ghosts])
        
