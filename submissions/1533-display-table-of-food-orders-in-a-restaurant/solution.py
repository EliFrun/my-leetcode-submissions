class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        ret = [["Table"]]
        tables = {}
        dishes = set()
        for name, table, dish in orders:
            dishes.add(dish)
            if table not in tables:
                tables[table] = {}
            tables[table][dish] = tables[table].get(dish, 0) + 1
        ret[0] += sorted(list(dishes))
        for table, counts in sorted(list(tables.items()), key=lambda x: int(x[0])):
            row = [table]
            for dish in ret[0][1:]:
                row.append(str(counts.get(dish, 0)))
            ret.append(row)

        return ret
