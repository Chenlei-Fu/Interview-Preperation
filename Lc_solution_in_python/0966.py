class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """
        the trick is vowel part
        since the vowels ('a', 'e', 'i', 'o', 'u') can be replaced
        they can be translated into *
        """
        def translate(word):
            return ''.join('*' if c in 'aeiou' else c for c in word.lower())
    
        def check(word):
            if word in wordSet:
                return word
            word_lower = word.lower()
            word_vowel = translate(word)
            if word_lower in capi:
                return capi[word_lower]
            if word_vowel in vowel:
                return vowel[word_vowel]
            return ''
        
        wordSet = set(wordlist)
        capi = {w.lower() :w for w in wordlist[::-1]}
        vowel = {translate(w): w for w in wordlist[::-1]}
        return [check(w) for w in queries]
