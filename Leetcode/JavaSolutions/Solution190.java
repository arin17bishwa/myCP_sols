package Leetcode.JavaSolutions;

public class Solution190 {
    class Solution {
        public int reverseBits(int n) {
            int ans = 0;
            for (int i = 0; i < 31; i++) {
                ans |= n & 1;
                n >>= 1;
                ans <<= 1;
            }
            return ans;
        }
    }

    public static void main(String[] args) {
        var cl = new Solution190();
        var obj = cl.new Solution();

        int n = 43261596;

        int ans = obj.reverseBits(n);
        System.out.println(ans);

    }
}
