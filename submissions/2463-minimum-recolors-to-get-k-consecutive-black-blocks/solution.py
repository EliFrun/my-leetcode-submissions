class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        ret = float('inf')
        for i, c in enumerate(blocks):
            if c == 'W':
                count += 1
            if i >= k:
                if blocks[i - k] == 'W':
                    count -= 1
            
            if i >= k - 1:
                ret = min(ret, count)

        ret = min(ret, count)
        return ret


