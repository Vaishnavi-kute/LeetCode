class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)              # Count frequencies
        max_freq = max(freq.values())     # Find maximum frequency
        total = sum(count for count in freq.values() if count == max_freq)
        return total