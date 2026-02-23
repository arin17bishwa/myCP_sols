package JavaSolutions;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ChocolateDistributionProblem3825 {

    class Solution {
        public int findMinDiff(ArrayList<Integer> arr, int m) {
            // your code here
            Collections.sort(arr);
            int n = arr.size();
            int ans = arr.get(n - 1) - arr.get(0);

            for (int i = m - 1; i < n; i++) {
                ans = Math.min(ans, arr.get(i) - arr.get(i - m + 1));
            }

            return ans;
        }
    }

    public static void main(String[] args) {
        var cl = new ChocolateDistributionProblem3825();
        var obj = cl.new Solution();

        ArrayList<Integer> arr = new ArrayList<>(List.of(3, 4, 1, 9, 56, 7, 9, 12));
        int m = 5;

        var ans = obj.findMinDiff(arr, m);
    }
}
