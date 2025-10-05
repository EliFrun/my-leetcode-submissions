class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        can_reach = [[set() for _ in range(len(heights[0]))] for _ in range(len(heights))]

        curr1 = set()
        curr2 = set()
        for i in range(len(heights)):
            curr1.add((i,0))
            curr2.add((i, len(heights[0]) - 1))
        
        for j in range(len(heights[0])):
            curr1.add((0, j))
            curr2.add((len(heights) - 1, j))

        def bfs(label, curr):
            dirs = [0,1,0,-1,0]
            visited = set()
            while curr:
                nxt = set()
                visited |= curr
                for i, j in curr:
                    can_reach[i][j].add(label)
                    for k in range(4):
                        di, dj = dirs[k], dirs[k + 1]
                        if not 0 <= i + di < len(heights):
                            continue
                        if not 0 <= j + dj < len(heights[0]):
                            continue
                        if (i + di, j + dj) in visited:
                            continue
                        if heights[i][j] > heights[i + di][j + dj]:
                            continue
                        nxt.add((i + di, j + dj))
                
                curr = nxt

        bfs(1, curr1)
        bfs(2, curr2)

        ret = []
        for i in range(len(can_reach)):
            for j in range(len(can_reach[0])):
                if len(can_reach[i][j]) > 1:
                    ret.append([i, j])

        return ret

                    

        
