class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        pre_trie = {}
        suf_trie = {}
        ret = 0
        for i, word in enumerate(words):
            curr = pre_trie
            pre = defaultdict(int)
            seq = ''
            for c in word:
                seq += c
                if c not in curr:
                    curr[c] = { 'word': 0 }
                curr = curr[c]
                if v := curr.get('word', None):
                    pre[seq] = v
            curr['word'] += 1

            curr = suf_trie
            suf = defaultdict(int)
            seq = ''
            for c in word[::-1]:
                seq += c
                if c not in curr:
                    curr[c] = { 'word': 0 }
                curr = curr[c]
                if v := curr.get('word', None):
                    suf[seq[::-1]] = v
            curr['word'] += 1

            for k in pre.keys():
                ret += min(pre.get(k, 0), suf.get(k, 0))

        return ret
                


        
        
