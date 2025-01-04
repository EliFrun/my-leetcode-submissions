class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if len(a) > len(b):
            if b in a:
                return 1
            if b in a + a:
                return 2
            return -1
        else:
            num_repeats = int(len(b) / len(a) + 0.999999)
            aa = a * num_repeats
            if b in aa:
                return num_repeats
            if b in aa + a:
                return num_repeats + 1
            if b in aa + a + a:
                return num_repeats + 2
            return -1
