class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        return [c for (c,b) in sorted([(c,b) for c,b,i in zip(code, businessLine, isActive) if i and c and b in ["electronics", "grocery", "pharmacy", "restaurant"] and all(x.isalnum() or x == '_' for x in c)], key=lambda x: (x[1], x[0]))]
        
