class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        d = defaultdict(list)
        for word in products:
            for i in range(1,len(word) + 1):
                d[word[:i]].append(word)

        for _,v in d.items():
            v.sort()

        return [d[searchWord[:i]][:3] for i in range(1, len(searchWord) + 1)]
        
