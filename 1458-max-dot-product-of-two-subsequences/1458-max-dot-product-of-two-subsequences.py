class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        
        dp = [[float('-inf')] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                product = nums1[i] * nums2[j]
                
                if i > 0 and j > 0:
                    dp[i][j] = max(
                        product,
                        product + max(0, dp[i-1][j-1]),
                        dp[i-1][j],
                        dp[i][j-1]
                    )
                elif i > 0:
                    dp[i][j] = max(product, dp[i-1][j])
                elif j > 0:
                    dp[i][j] = max(product, dp[i][j-1])
                else:
                    dp[i][j] = product
        
        return dp[n-1][m-1]
        