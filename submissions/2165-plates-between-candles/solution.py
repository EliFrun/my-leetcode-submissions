class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        candles = SortedList()
        prefix = {}
        count = 0
        for i, c in enumerate(s):
            if c == '*':
                count += 1
            else:
                candles.add(i)
                prefix[i] = count

        ret = []
        for l, r in queries:
            left_idx = candles.bisect_left(l)
            if left_idx >= len(candles):
                ret.append(0)
                continue
            if candles[left_idx] < l:
                left_idx += 1
            
            right_idx = candles.bisect_right(r)
            if right_idx >= len(candles) or candles[right_idx] != r:
                right_idx -= 1
            if left_idx >= right_idx:
                ret.append(0)
            else:
                ret.append(prefix[candles[right_idx]] - prefix[candles[left_idx]])

        return ret
        
