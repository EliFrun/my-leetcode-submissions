class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        colors = {}
        ret = [0] * len(queries)
        for i, (ball, color) in enumerate(queries):
            colors[color] = colors.get(color, 0) + 1
            if ball in balls:
                c = balls[ball]
                colors[c] -= 1
                if colors[c] == 0:
                    colors.pop(c)
            balls[ball] = color
            
            ret[i] = len(colors.keys())

        return ret
        
