class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            for i in range(len(row) - 2, -1, -1):
                if row[i] == "#":
                    for j in range(i, len(row) - 1):
                        if row[j + 1] == ".":
                            row[j] = '.'
                            row[j + 1] = '#'
                        else:
                            break
                            
        return [[box[len(box) - 1 - j][i] for j in range(len(box))] for i in range(len(box[0]))]
