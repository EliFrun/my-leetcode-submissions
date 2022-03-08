class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join([x[0].upper() + x[1:].lower() if len(x) > 2 else x.lower() for x in title.split(" ")])
        
