class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        d1 = set(wordlist)
        
        d2 = {}
        for word in wordlist:
            if word.lower() in d2:
                continue
            d2[word.lower()] = word

        d3 = {}
        for word in wordlist:
            word2 = word.lower().replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*')
            if word2 in d3:
                continue
            d3[word2] = word

        ret = []
        for word in queries:
            if word in d1:
                ret.append(word)
                continue

            if word.lower() in d2:
                ret.append(d2[word.lower()])
                continue

            word2 = word.lower().replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*')
            if word2 in d3:
                ret.append(d3[word2])
                continue     

            ret.append('')
        return ret
            
                
        
