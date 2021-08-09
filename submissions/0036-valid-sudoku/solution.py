class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = board
        columns = [
            [""] * 9,[""] * 9,[""] * 9,
            [""] * 9,[""] * 9,[""] * 9,
            [""] * 9,[""] * 9,[""] * 9
        ]
        
        
        for i in range(0, 9):
            for j in range(0, 9):
                columns[j][i] = rows[i][j]




        ranges = [
            ((0,3),(0,3)),((3,6),(0,3)),((6,9),(0,3)),
            ((0,3),(3,6)),((3,6),(3,6)),((6,9),(3,6)),
            ((0,3),(6,9)),((3,6),(6,9)),((6,9),(6,9))
        ]
        
        boxes = [
            [""] * 9,[""] * 9,[""] * 9,
            [""] * 9,[""] * 9,[""] * 9,
            [""] * 9,[""] * 9,[""] * 9
        ]
        index_1 = 0
        for b in ranges:
            index_2 = 0
            for i in range(*b[0]):
                for j in range(*b[1]):
                    boxes[index_1][index_2] = board[i][j]
                    index_2 += 1
            index_1 += 1
                    
                    
        for row in rows:
            row = list(filter(lambda a: a != '.', row))
            if not len(row) == len(list(set(row))):
                return False
    
        for column in columns:
            column = list(filter(lambda a: a != '.', column))
            if not len(column) == len(list(set(column))):
                return False
                
        for box in boxes:
            box = list(filter(lambda a: a != '.', box))
            if not len(box) == len(list(set(box))):
                return False
        
        
        
        return True
                    

        
