class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def to_tuple(word):
            even = [0] * 26
            odd = [0] * 26
            for i in range(0, len(word), 2):
                even[ord(word[i]) - ord('a')] += 1
                if i + 1 < len(word):
                    odd[ord(word[i + 1]) - ord('a')] += 1
            
            return (tuple(even), tuple(odd))


        ret = set()
        for word in words:
            ret.add(to_tuple(word))

        return len(ret)
        
