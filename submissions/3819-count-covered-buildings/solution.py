class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rows = defaultdict(SortedList)
        columns = defaultdict(SortedList)

        for x,y in buildings:
            rows[x].add(y)
            columns[y].add(x)


        ret = 0
        for x,y in buildings:
            if not 0 < rows[x].bisect_left(y) < len(rows[x]) - 1:
                continue
            if not 0 < columns[y].bisect_left(x) < len(columns[y]) - 1:
                continue
            ret += 1
        return ret


