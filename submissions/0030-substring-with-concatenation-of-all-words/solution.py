class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        c = Counter(words)
        ret = []
        for i in range(len(words[0])):
            st = []
            for j in range(i, len(s), len(words[0])):
                st.append(s[j:j + len(words[0])])
            left = 0
            contains = defaultdict(int)
            for j, word in enumerate(st):
                if word in c:
                    contains[word] += 1
                    while contains[word] > c[word]:
                        contains[st[left]] -= 1
                        left += 1
                    if all(c[k] == contains[k] for k in c.keys()):
                        ret.append(i + len(words[0]) * left)
                else:
                    contains = defaultdict(int)
                    left = j + 1
        return ret


        
