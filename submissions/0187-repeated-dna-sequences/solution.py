class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counter = defaultdict(int)
        curr = ''
        for c in s:
            if len(curr) < 10:
                curr += c
            else:
                curr = curr[1:] + c

            counter[curr] += 1

        return [k for k,v in counter.items() if v > 1]
        
