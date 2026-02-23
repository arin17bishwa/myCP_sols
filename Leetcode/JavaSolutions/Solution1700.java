package Leetcode.JavaSolutions;

import java.util.Arrays;

public class Solution1700 {
    class Solution {
        public int countStudents(int[] students, int[] sandwiches) {
            int n = students.length;
            int ones = Arrays.stream(students).sum();
            int[] cnt = {n - ones, ones};
            int ans = n;

            for (int ele : sandwiches) {
                if (cnt[ele] < 1)
                    break;
                ans--;
                cnt[ele]--;
            }
            return ans;

        }
    }

    public static void main(String[] args) {
        var cl = new Solution1700();
        var obj = cl.new Solution();

//        int[] l1 = {1, 1, 0, 0};
//        int[] l2 = {0, 1, 0, 1};

        int[] l1 = {1, 1, 1, 0, 0, 1};
        int[] l2 = {1, 0, 0, 0, 1, 1};

        var ans = obj.countStudents(l1, l2);

        System.out.println(ans);

    }

}
