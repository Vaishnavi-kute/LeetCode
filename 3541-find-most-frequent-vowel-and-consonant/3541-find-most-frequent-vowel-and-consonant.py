class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set("aeiou")
        freq = Counter(s)   # frequency of each character

        # collect vowel and consonant frequencies
        vowel_freqs = [count for ch, count in freq.items() if ch in vowels]
        consonant_freqs = [count for ch, count in freq.items() if ch not in vowels]

        # get maximum or 0 if none
        max_vowel = max(vowel_freqs, default=0)
        max_consonant = max(consonant_freqs, default=0)

        return max_vowel + max_consonant

        