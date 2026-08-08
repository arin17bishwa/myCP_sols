package Leetcode.JavaSolutions;

import java.util.Arrays;

public class Solution338 {
    class Solution {
        public int[] countBits(int n) {
            int[] ans = new int[n + 1];

            if (n == 0)
                return ans;

            int highestPower = 1;

            for (int i = 1; i <= n; i++) {
                if ((highestPower << 1) <= i)
                    highestPower <<= 1;
                ans[i] = ans[i - highestPower] + 1;
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
