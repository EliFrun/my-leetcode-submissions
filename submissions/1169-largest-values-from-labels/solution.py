class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        arr = []
        for i in range(len(values)):
            arr.append((values[i], labels[i]))
            
        arr.sort(reverse=True)
        
        count = defaultdict(int)
        curr = 0
        i = 0
        ret = 0
        while curr < numWanted and i < len(arr):
            if count[arr[i][1]] < useLimit:
                ret += arr[i][0]
                count[arr[i][1]] += 1
                curr += 1
            
            i += 1
            
        return ret
