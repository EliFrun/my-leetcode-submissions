class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 1:
            return [0] if s == words[0] and len(words) == 1 else []
        
        ret = []
        for i in range(len(words[0])):
            ret.extend(self.helper(s[i:], words, i))
            
        ret.sort()
        return ret
    
    
    
    def helper(self, s, words, shift):
        q = deque()
        
        length = len(words[0])
        
        parse = []
        
        word = ""
        for j in s:
            if len(word) < length:
                word += j
            else:
                parse.append(word)
                word = j
                
        parse.append(word)
        ret = []  
        i = 1
        for word in parse:
            if len(q) < len(words):
                if word in q and q.count(word) == words.count(word):
                    while q.popleft() != word:
                        continue
                if word in words:
                    q.append(word)
                else:
                    q = deque()

            if len(q) == len(words):
                ret.append((i - len(words)) * length + shift)
                q.popleft()
            
            i += 1
            
            
        return ret
