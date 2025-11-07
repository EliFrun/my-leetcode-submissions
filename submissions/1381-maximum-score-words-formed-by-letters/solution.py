class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        l = [0] * 26
        for c in letters:
            l[ord(c) - ord('a')] += 1
        def solve(i):
            ret = 0
            for i in range(i, len(words)):
                wc = Counter(words[i])
                can_use = True
                for k in wc.keys():
                    if wc[k] > l[ord(k) - ord('a')]:
                        can_use = False
                        break
                
                if can_use:
                    for k in words[i]:
                        l[ord(k) - ord('a')] -= 1
                    word_score = sum([score[ord(c) - ord('a')] for c in words[i]])
                    ret = max(ret, word_score + solve(i + 1))
                    for k in words[i]:
                        l[ord(k) - ord('a')] += 1
            return ret

        return solve(0)
                    
        
