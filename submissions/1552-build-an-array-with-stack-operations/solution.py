class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        curr = 1
        ret = []
        for i in target:
            while curr < i:
                ret.extend(["Push", "Pop"])
                curr += 1
            ret.append("Push")
            curr += 1
        return ret
        
        
