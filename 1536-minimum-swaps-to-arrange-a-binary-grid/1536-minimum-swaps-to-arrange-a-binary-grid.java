class Solution {
    public int minSwaps(int[][] grid) {
        int n = grid.length;
        int[] trailingZeros = new int[n];

        // Step 1: Count trailing zeros for each row
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = n - 1; j >= 0; j--) {
                if (grid[i][j] == 0) count++;
                else break;
            }
            trailingZeros[i] = count;
        }

        int swaps = 0;

        // Step 2: Greedy row swapping
        for (int i = 0; i < n; i++) {
            int requiredZeros = n - i - 1;
            int j = i;

            // Find a row below with enough trailing zeros
            while (j < n && trailingZeros[j] < requiredZeros) {
                j++;
            }

            if (j == n) return -1; // Not possible

            // Bring row j to position i
            while (j > i) {
                int temp = trailingZeros[j];
                trailingZeros[j] = trailingZeros[j - 1];
                trailingZeros[j - 1] = temp;
                swaps++;
                j--;
            }
        }

        return swaps;
    }
}