package Leetcode.JavaSolutions;

import java.util.Arrays;

public class Solution338 {
    class Solution {
        public int[] countBits(int n) {
            int[] ans = new int[n + 1];

            for (int i = 0; i <= n; i++) {
                ans[i] = countSetBits(i);
            }
            return ans;
        }

        public int countSetBits(Integer n) {
            int ans = 0;
            while (n > 0) {
                ans += (n & 1);
                n >>= 1;
            }
            return ans;
        }
    }

    public static void main(String[] args) {
        var cl = new Solution338();
        var obj = cl.new Solution();
        int n;

        n = 5;

        int[] ans = obj.countBits(n);
        System.out.println(Arrays.toString(ans));

    }
}
