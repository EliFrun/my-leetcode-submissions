class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = defaultdict(int)
        

    def setCell(self, cell: str, value: int) -> None:
        self.rows[cell] = value
        

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)
        

    def getValue(self, formula: str) -> int:
        left, right = formula.split('+')[0].split('=')[1], formula.split('+')[1]
        return self._f(left) + self._f(right)


    def _letter_to_column(self, letter):
        return ord(letter) - ord('A')

    def _f(self, v):
        if v[0].isnumeric():
            return int(v)
        
        return self.rows[v]
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
