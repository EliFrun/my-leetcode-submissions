class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        return (sentence := sentence.split(' ')) and all(sentence[i][-1] == sentence[(i + 1)% len(sentence)][0] for i in range(len(sentence)))
        
