package Leetcode.JavaSolutions;

public class Solution1404 {
    class Solution {
        public int numSteps(String s) {
            int ops = 0, carry = 0;

            for (int i = s.length() - 1; i > 0; i--) {
                if (((s.charAt(i) - '0' + carry) & 1) == 0) {
                    ops++;
                } else {
                    ops += 2;
                    carry = 1;
                }
            }

            return ops + carry;
        }
    }

    public static void main(String[] args) {
        var cl = new Solution1404();
        var obj = cl.new Solution();
        String s;

        s = "1101";
        s = "10";
        s = "1";

        int ans = obj.numSteps(s);
        System.out.println(ans);

    }
}
