class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]  # take first string as reference
        
        for word in strs[1:]:
            # shrink prefix until it matches the beginning of word
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

        