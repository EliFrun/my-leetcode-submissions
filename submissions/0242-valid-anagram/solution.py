class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = Counter(s)
        tt = Counter(t)

        for k in set(ss.keys()).union(set(tt.keys())):
            if ss.get(k, 0) != tt.get(k, 0):
                return False

        return True
        
