package JavaSolutions;

public class MaxCircularSubarraySum_1587115620 {
    class Solution {
        public int maxCircularSum(int[] arr) {
            int minSubarraySum = 0;
            int maxSubarraySum = 0;
            int minCurr = 0;
            int maxCurr = 0;
            int total = 0;
            int mx = arr[0];

            for (int ele : arr) {
                total += ele;
                mx = Math.max(mx, ele);

                minCurr += ele;
                maxCurr += ele;

                minCurr = Math.min(0, minCurr);
                maxCurr = Math.max(0, maxCurr);

                minSubarraySum = Math.min(minSubarraySum, minCurr);
                maxSubarraySum = Math.max(maxSubarraySum, maxCurr);

            }

            int ans = Math.max(maxSubarraySum, total - minSubarraySum);
            return ans == 0 ? mx : ans;
        }
    }

    public static void main(String[] args) {
        var cl = new MaxCircularSubarraySum_1587115620();
        var obj = cl.new Solution();

        int[] arr = {8, -8, 9, -9, 10, -11, 12};

        var ans = obj.maxCircularSum(arr);

        System.out.println(ans);

    }


}
