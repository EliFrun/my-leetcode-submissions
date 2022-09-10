class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = 'aeiou'
        wordlistMap = {}
        for idx, word in enumerate(wordlist):
            wordlistMap[word] = idx
            
        lowerWordlistMap = {}
        for idx, word in enumerate(wordlist):
            if word.lower() not in lowerWordlistMap:
                lowerWordlistMap[word.lower()] = idx
                
        vowellessMap = {}
        
        for idx, word in enumerate(wordlist):
            a = ''.join([x if x not in vowels else '*' for x in word.lower()])
            if a not in vowellessMap:
                vowellessMap[a] = idx
                
                
        ret = [''] * len(queries)
        for i, query in enumerate(queries):
            if query in wordlistMap:
                ret[i] = wordlist[wordlistMap[query]]
                continue
                
            if query.lower() in lowerWordlistMap:
                ret[i] = wordlist[lowerWordlistMap[query.lower()]]
                continue
             
            vowellessWord = ''.join([x if x not in vowels else '*' for x in query.lower()])
            if vowellessWord in vowellessMap:
                ret[i] = wordlist[vowellessMap[vowellessWord]]
                
        return ret
            
                
        
