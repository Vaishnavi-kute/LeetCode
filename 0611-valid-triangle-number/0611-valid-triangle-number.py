class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array to use triangle inequality efficiently
        n = len(nums)
        count = 0

        # Fix the largest side (c) at index k
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1  # Two pointers for the smaller two sides
            while i < j:
                # Triangle condition: a + b > c
                if nums[i] + nums[j] > nums[k]:
                    # If nums[i] + nums[j] > nums[k], then all pairs (i...j-1, j) will also work
                    count += (j - i)
                    j -= 1  # Try smaller 'b' to check for more pairs
                else:
                    i += 1  # Need a larger sum, so move 'a' forward

        return count

        