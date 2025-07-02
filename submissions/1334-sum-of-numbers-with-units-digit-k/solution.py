class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        base = [x + k for x in range(0, num + 1, 10)]
        curr = set(base)
        visited = set()
        layer = 0
        while curr:
            layer += 1
            nxt = set()
            for v in curr:
                if v == num:
                    return layer
                visited.add(v)
                if v + k <= num:
                    nxt.add(v + k)

            curr = nxt - visited

        return -1
