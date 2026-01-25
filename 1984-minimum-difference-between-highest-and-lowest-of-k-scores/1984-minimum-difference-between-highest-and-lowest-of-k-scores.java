import java.util.Arrays;

class Solution {
    public int minimumDifference(int[] nums, int k) {
        // If only one student is selected
        if (k == 1) {
            return 0;
        }

        // Sort the array
        Arrays.sort(nums);

        int minDiff = Integer.MAX_VALUE;

        // Sliding window of size k
        for (int i = 0; i <= nums.length - k; i++) {
            int diff = nums[i + k - 1] - nums[i];
            minDiff = Math.min(minDiff, diff);
        }

        return minDiff;
    }
}
