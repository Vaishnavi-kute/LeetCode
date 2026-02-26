class Solution {
    public int numSteps(String s) {
        int steps = 0;
        int carry = 0;

        // start from last bit, stop before first bit
        for (int i = s.length() - 1; i > 0; i--) {
            int bit = (s.charAt(i) - '0') + carry;

            if (bit % 2 == 0) {
                // even
                steps += 1;
            } else {
                // odd
                steps += 2;
                carry = 1;
            }
        }

        // if carry remains at MSB
        if (carry == 1) {
            steps += 1;
        }

        return steps;
  
    }
}