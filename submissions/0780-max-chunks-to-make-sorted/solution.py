class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ret = []
        curr = set()
        mi = 0
        for i in range(len(arr)):
            curr.add(arr[i])
            if all([x in curr for x in range(mi, i + 1)]):
                ret.append(curr)
                curr = set()
                mi = i + 1
            
        #ret.append(curr)
        #print(ret)
        return len(ret)
