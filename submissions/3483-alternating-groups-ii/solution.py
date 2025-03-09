class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        i = 1
        seq = []
        curr = colors[0]
        count = 1
        while i < len(colors):
            if colors[i] != curr:
                count += 1
            else:
                seq.append(count)
                count = 1
            curr = colors[i]
            i += 1
        if colors[-1] != colors[0]:
            if len(seq) > 0:
                seq.append(count + (seq[0] if seq[0] < k else (k - 1)))
            else:
                seq.append(count + min(count, k) - 1)
        else:
            seq.append(count)
        #print(seq)
        
        return sum([max(0, x - k + 1) for x in seq])
        
