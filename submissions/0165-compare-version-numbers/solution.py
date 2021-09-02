class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        for x, y in zip(v1, v2):
            if int(x) == int(y):
                continue
            else:
                return -1 if int(x) < int(y) else 1
        
        if len(v1) < len(v2):
            return 0 if all([int(x) == 0 for x in v2[len(v1):]]) else -1
        elif len(v1) > len(v2):
            return 0 if all([int(x) == 0 for x in v1[len(v2):]]) else 1
        
        return 0
