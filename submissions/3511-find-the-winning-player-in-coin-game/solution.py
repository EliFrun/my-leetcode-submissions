class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        p = 1
        while x >= 1 and y >= 4:
            x -= 1
            y -= 4
            p = 1 - p
        return "Alice" if p == 0 else "Bob"
            
        
