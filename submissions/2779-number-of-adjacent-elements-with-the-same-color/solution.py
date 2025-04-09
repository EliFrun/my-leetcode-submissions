class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        arr = [0] * n
        ret = []
        v = 0
        for idx, col in queries:
            left = arr[idx - 1]  if idx > 0 else 0
            right = arr[idx + 1] if idx < len(arr) - 1 else 0
            curr = arr[idx]
            c = 0
            if curr != 0 and curr == left:
                c += 1
            if curr != 0 and curr == right:
                c += 1
            arr[idx] = col
            curr = col
            if curr == left:
                c -= 1
            if curr == right:
                c -= 1
            v -= c
            ret.append(v)

        return ret
        
