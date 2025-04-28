class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        c = Counter([x.lower() for x in paragraph.replace("!", " ").replace("?", " ").replace("'", " ").replace(",", " ").replace(";", " ").replace(".", "").split(' ')])
        m = 0
        ret = ""
        for k,v in c.items():
            if not k:
                continue
            if k in banned:
                continue
            if v > m:
                ret = k
                m = v
        return ret

        
        
