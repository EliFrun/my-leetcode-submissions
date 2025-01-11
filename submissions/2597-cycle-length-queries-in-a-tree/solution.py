class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def depth(val):
            return int(log2(val))

        def gca(a, b):
            if a == b:
                return int(log2(a)) - 1
            while int(log2(a)) > int(log2(b)):
                a = a >> 1
            while int(log2(b)) > int(log2(a)):
                b = b >> 1

            while a != b:
                a = a >> 1
                b = b >> 1
            return a

        return [depth(a) + depth(b) + 1 - 2 * depth(gca(a,b)) for a,b in queries]
        
