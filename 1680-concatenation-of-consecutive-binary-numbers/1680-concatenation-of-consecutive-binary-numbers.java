class Solution {
    public int concatenatedBinary(int n) {
        long ans = 0;
        int MOD = 1_000_000_007;
        int bits = 0;

        for(int i = 1; i <= n; i++){
            //Check if i is a power of 2 
            if (( i & (i - 1))== 0){
                bits++;
            }
            ans = ((ans << bits) + i) % MOD;
        }
        return (int) ans;
    }
}