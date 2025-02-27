class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words2 = [Counter(word) for word in set([''.join(sorted(w)) for w in words2])]
        letter_reqs = defaultdict(int)
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            for word in words2:
                letter_reqs[letter] = max(letter_reqs[letter], word[letter])
        def is_subset(w1, w2):
            w1 = Counter(w1)
            for key in w2.keys():
                if w2[key] > w1[key]:
                    return False
            return True


        return [word for word in words1 if is_subset(word, letter_reqs)]
        
