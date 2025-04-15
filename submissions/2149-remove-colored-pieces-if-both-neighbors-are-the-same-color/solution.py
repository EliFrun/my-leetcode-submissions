class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count = 0
        curr = colors[0]
        curr_count = 1
        for c in colors[1:]:
            if c == curr:
                curr_count += 1
            else:
                count += max(0, curr_count - 2) if curr == 'A' else - max(0, curr_count - 2)
                curr = c
                curr_count = 1

        count += max(0, curr_count - 2) if curr == 'A' else - max(0, curr_count - 2)

        return count > 0

        
