package Leetcode.JavaSolutions;

import java.util.Arrays;

public class Solution242 {
    class Solution {
        public boolean isAnagram(String s, String t) {
            if (s.length() != t.length())
                return false;

            var sArr = s.toCharArray();
            var tArr = t.toCharArray();
            Arrays.sort(sArr);
            Arrays.sort(tArr);
            return Arrays.equals(sArr, tArr);
        }
    }


    public static void main(String[] args) {
        var cl = new Solution242();

        var obj = cl.new Solution();

        String s = "racecar";
        String t = "carraca";

        var ans = obj.isAnagram(s, t);

        System.out.println(ans);

    }
}



