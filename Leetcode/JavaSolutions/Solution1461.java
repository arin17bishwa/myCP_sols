package Leetcode.JavaSolutions;

import java.util.HashSet;
import java.util.Set;

public class Solution1461 {

    class Solution {
        public boolean hasAllCodes(String s, int k) {
            int n = s.length();
            if (n < k)
                return false;
            int curr = 0;
            int mask = (1 << k) - 1;
            for (int i = 0; i < k; i++) {
                curr = (curr << 1) | (s.charAt(i) == '1' ? 1 : 0);
            }
            Set<Integer> seen = new HashSet<>(1 << k);
            seen.add(curr);

            for (int i = k; i < n; i++) {
                curr = (curr << 1) | (s.charAt(i) == '1' ? 1 : 0);
                curr &= mask;
                seen.add(curr);
            }

            return seen.size() == (1 << k);
        }
    }

    public static void main(String[] args) {
        var cl = new Solution1461();
        var obj = cl.new Solution();

        String s = "00110110";
        int k = 2;

        var ans = obj.hasAllCodes(s, k);

        System.out.println(ans);


    }
}
