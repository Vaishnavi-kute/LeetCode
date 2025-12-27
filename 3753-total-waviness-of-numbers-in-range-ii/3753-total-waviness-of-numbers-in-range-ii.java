import java.util.*;

class Solution {

    public long totalWaviness(long num1, long num2) {
        return solve(num2) - solve(num1 - 1);
    }

    private long solve(long x) {
        if (x < 0) return 0;
        char[] s = Long.toString(x).toCharArray();
        int n = s.length;

        Map<String, long[]> memo = new HashMap<>();

        return dfs(0, true, false, -1, -1, s, memo)[1];
    }

    // returns long[]{count, wavinessSum}
    private long[] dfs(int pos, boolean tight, boolean started,
                       int d1, int d2, char[] s,
                       Map<String, long[]> memo) {

        if (pos == s.length) {
            return new long[]{started ? 1 : 0, 0};
        }

        String key = pos + "|" + tight + "|" + started + "|" + d1 + "|" + d2;
        if (!tight && memo.containsKey(key)) return memo.get(key);

        int up = tight ? s[pos] - '0' : 9;
        long totalCount = 0, totalWaviness = 0;

        for (int d = 0; d <= up; d++) {
            boolean ntight = tight && (d == up);
            boolean nstarted = started || d != 0;

            int nd1 = d1, nd2 = d2;
            long add = 0;

            if (!nstarted) { // still leading zeros
                nd1 = nd2 = -1;
            } else if (!started) { // first real digit
                nd2 = d;
            } else if (d1 == -1) { // only one digit so far
                nd1 = d2;
                nd2 = d;
            } else { // at least two digits already placed
                // current middle digit is d2
                if ((d2 > d1 && d2 > d) || (d2 < d1 && d2 < d)) add = 1;

                nd1 = d2;
                nd2 = d;
            }

            long[] res = dfs(pos + 1, ntight, nstarted, nd1, nd2, s, memo);
            long cnt = res[0];
            long wav = res[1];

            totalCount += cnt;
            totalWaviness += wav + add * cnt;
        }

        if (!tight) memo.put(key, new long[]{totalCount, totalWaviness});
        return new long[]{totalCount, totalWaviness};
    }
}
