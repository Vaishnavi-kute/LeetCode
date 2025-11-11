class Solution(object):
    def findMaxForm(self, strs, m, n):
        # Initialize DP table 
        dp = [[0]* (n + 1) for _ in range (m + 1)]
        
        # Process each string
        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')

            #Traverse backwards to prevent double counting 
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1 ):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j- ones]+ 1 )
        
        return dp[m][n]




        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        