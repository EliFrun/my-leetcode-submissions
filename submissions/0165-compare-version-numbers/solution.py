class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1 = v1.split('.')
        v2 = v2.split('.')
        for i in range(max(len(v1), len(v2))):
            x = int(v1[i]) if len(v1) > i else 0
            y = int(v2[i]) if len(v2) > i else 0

            if x > y:
                return 1
            if y > x:
                return -1



        return 0
        
