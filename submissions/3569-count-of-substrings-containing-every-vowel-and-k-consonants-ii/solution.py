class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        counts = [[0,0,0,0,0,0]]
        curr = [0,0,0,0,0]
        indexes = [0]
        count = 0
        m = { 'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4 }
        for i,c in enumerate(word):
            if c in m:
                curr[m[c]] += 1
            else:
                count += 1
                indexes.append(i + 1)
            
            counts.append([count] + curr)

        start = 0
        ret = 0
        for i in range(len(counts)):
            count = counts[i]
            if count[0] - k < 0:
                continue
            start = indexes[count[0] - k]
            left = indexes[count[0] - k]
            right = 0
            if count[0] - k + 1 >= len(indexes):
                right = len(counts) - 1
            else:
                right = indexes[count[0] - k + 1] - 1
            while right - left > 1:
                middle = (left + right) // 2
                if all([count[j] - counts[middle][j] >= 1 for j in range(1, 6)]):
                    left = middle
                else:
                    right = middle

            if all([count[j] - counts[right][j] >= 1 for j in range(1, 6)]):
                ret += right - start + 1
            elif all([count[j] - counts[left][j] >= 1 for j in range(1, 6)]):
                ret += left - start + 1
            


        return ret
        
