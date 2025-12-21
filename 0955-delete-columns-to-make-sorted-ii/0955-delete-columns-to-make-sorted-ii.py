class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        deleted = 0
        sorted_flag = [False] * (n - 1)
        
        for col in range(m):
            # Check if this column violates lexicographic order
            bad = False
            for i in range(n - 1):
                if not sorted_flag[i] and strs[i][col] > strs[i + 1][col]:
                    bad = True
                    break
            
            if bad:
                deleted += 1
                continue
            
            # Update sorted_flag where order is determined
            for i in range(n - 1):
                if not sorted_flag[i] and strs[i][col] < strs[i + 1][col]:
                    sorted_flag[i] = True
        
        return deleted

        