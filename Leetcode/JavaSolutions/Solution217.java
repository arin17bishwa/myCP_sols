package Leetcode.JavaSolutions;

import java.util.HashSet;


class Solution {
    public boolean containsDuplicate(int[] nums) {
        var seen = new HashSet<>();

        for (int num : nums) {
            if (seen.contains(num))
                return true;
            seen.add(num);
        }

        return false;
    }
}


public class Solution217 {
    public static void main(String[] args) {
        var obj = new Solution();

        int[] arr = {1, 2, 3};

        boolean ans = obj.containsDuplicate(arr);

        System.out.println(ans);

    }

}

