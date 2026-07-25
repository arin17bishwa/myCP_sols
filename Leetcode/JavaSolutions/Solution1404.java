package Leetcode.JavaSolutions;

public class Solution1404 {
    class Solution {
        public int numSteps(String s) {
            int ans = 0;
            StringBuilder sb = new StringBuilder(s);

            while (sb.length() > 1) {
                ans++;

                int n = sb.length();
                if (sb.charAt(n - 1) == '0') {
                    sb.deleteCharAt(n - 1);
                } else {
                    int idx = n - 1;
                    while (idx >= 0 && sb.charAt(idx) == '1') {
                        sb.setCharAt(idx, '0');
                        idx--;
                    }

                    if (idx >= 0) {
                        sb.setCharAt(idx, '1');
                    } else {
                        sb.insert(0, '1');
                    }
                }
            }

            return ans;
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
