class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        def solve(count):
            curr = 0
            ret = []
            for i in range(1, count + 1):
                if curr >= len(message):
                    return -1
                suffix_size = len(str(i)) + 3 + len(str(count))
                ret.append(message[curr:curr+limit - suffix_size] + f'<{i}/{count}>')
                curr += limit - suffix_size
            if curr < len(message):
                return 1
            return ret

        for p in range(0, 4):
            left, right = 10 ** p, 10 ** (p + 1)
            while left <= right:
                middle = (left + right) // 2
                res = solve(middle)
                if res == -1:
                    right = middle - 1
                elif res == 1:
                    left = middle + 1
                else:
                    return res

        return []

        
