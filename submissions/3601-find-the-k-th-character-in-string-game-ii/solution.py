class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        k = bin(k - 1)[2:]
        operations = operations[:len(k)]
        shifts = 0
        for v, o in zip(k, operations[::-1]):
            shifts += int(v) & int(o)

        return chr(ord('a') + (shifts % 26))

