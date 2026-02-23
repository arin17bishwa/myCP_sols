package JavaSolutions;

import java.util.Arrays;

public class AttendAllMeetings {

    class Solution {
        static boolean canAttend(int[][] arr) {
            int n = arr.length;
            Arrays.sort(arr, (a, b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);

            for (int i = 1; i < n; i++) {
                if (arr[i - 1][1] > arr[i][0])
                    return false;
            }
            return true;
        }
    }

    public static void main(String[] args) {

//        int[][] arr = {{1, 4}, {10, 15}, {7, 10}};
        int[][] arr = {{2, 4}, {9, 12}, {6, 10}};

        var ans = Solution.canAttend(arr);

        System.out.println(ans);
    }

}
