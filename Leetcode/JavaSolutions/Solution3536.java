package Leetcode.JavaSolutions;

public class Solution3536 {
    class Solution {
        public int maxProduct(int n) {
            int first = 0, second = 0;
            int dig;
            while (n > 0) {
                dig = n % 10;
                if (dig > first) {
                    second = first;
                    first = dig;
                } else if (dig > second) {
                    second = dig;
                }
                n /= 10;
            }
            return first * second;
        }
    }


    public static void main(String[] args) {
        var cl = new Solution3536();
        var obj = cl.new Solution();
        int n;

        n = 31;

        int ans = obj.maxProduct(n);
        System.out.println(ans);

    }
}
