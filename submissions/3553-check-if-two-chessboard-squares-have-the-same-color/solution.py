class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        return ('abcdefgh'.index(coordinate1[0]) + int(coordinate1[1])) % 2 ==  ('abcdefgh'.index(coordinate2[0]) + int(coordinate2[1])) % 2 
        
