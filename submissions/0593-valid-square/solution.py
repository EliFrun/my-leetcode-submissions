class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        distances = [
            sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2),
            sqrt((p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2),
            sqrt((p1[0] - p4[0]) ** 2 + (p1[1] - p4[1]) ** 2),
            sqrt((p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2),
            sqrt((p2[0] - p4[0]) ** 2 + (p2[1] - p4[1]) ** 2),
            sqrt((p3[0] - p4[0]) ** 2 + (p3[1] - p4[1]) ** 2)
        ]

        distances.sort()
        return all([d == distances[0] for d in distances[:4]]) and distances[4] == distances[5] and distances[0] != distances[-1]
        
