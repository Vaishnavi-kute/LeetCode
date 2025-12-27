class Solution {
    public int[] lexSmallestNegatedPerm(int n, long target) {

        long total = (long) n * (n + 1) / 2;

        // Feasibility checks
        if (Math.abs(target) > total) return new int[0];
        if (((total - target) & 1L) == 1L) return new int[0];

        long negSum = (total - target) / 2;

        boolean[] neg = new boolean[n + 1];
        long remain = negSum;

        // choose negatives greedily from largest to smallest
        for (int k = n; k >= 1 && remain > 0; k--) {
            if (k <= remain) {
                neg[k] = true;
                remain -= k;
            }
        }

        if (remain != 0) return new int[0]; // safety, though greedy guarantees this

        int[] res = new int[n];
        int idx = 0;

        // negatives in increasing order (i.e., -n, -(n-1), ...)
        for (int k = n; k >= 1; k--) {
            if (neg[k]) res[idx++] = -k;
        }

        // then positives in increasing order
        for (int k = 1; k <= n; k++) {
            if (!neg[k]) res[idx++] = k;
        }

        return res;
    }
}
