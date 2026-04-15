class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_distance = float('inf')
        
        for i in range(n):
            if words[i] == target:
                # distance moving right
                right = (i - startIndex + n) % n
                
                # distance moving left
                left = (startIndex - i + n) % n
                
                min_distance = min(min_distance, right, left)
        
        if min_distance == float('inf'):
            return -1
        
        return min_distance