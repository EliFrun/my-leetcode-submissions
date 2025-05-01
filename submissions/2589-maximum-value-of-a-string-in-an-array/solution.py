class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max([len(x) if not x.isnumeric() else int(x) for x in strs])
        
