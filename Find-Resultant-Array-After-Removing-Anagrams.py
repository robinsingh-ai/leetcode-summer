class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        prev = ""
        for word in words:
            sorted_word = ''.join(sorted(word))
            if sorted_word!= prev:
                result.append(word)
                prev = sorted_word
        return result
                