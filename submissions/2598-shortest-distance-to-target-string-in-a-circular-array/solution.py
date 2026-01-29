class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ret = float('inf')
        for i, word in enumerate(words):
            if word == target:
                ret = min(ret, abs(startIndex - i))
                ret = min(ret, startIndex + len(words) - i)
                ret = min(ret, i + len(words) - startIndex)


        return ret if ret != float('inf') else -1
            
        

        
