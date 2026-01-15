class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        vowel_chars = []
        
        # Collect vowels
        for ch in s:
            if ch in vowels:
                vowel_chars.append(ch)
        
        # Sort vowels by ASCII
        vowel_chars.sort()
        
        # Rebuild string
        result = []
        idx = 0
        for ch in s:
            if ch in vowels:
                result.append(vowel_chars[idx])
                idx += 1
            else:
                result.append(ch)
        
        return "".join(result)
