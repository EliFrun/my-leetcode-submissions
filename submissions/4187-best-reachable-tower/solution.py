class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        towers = [x for x in towers if abs(x[0] - center[0]) + abs(x[1] - center[1]) <= radius]
        towers.sort(key=lambda x: (-x[2], x[0], x[1]))
        if towers:
            return [towers[0][0], towers[0][1]]
        return [-1, -1]
        
