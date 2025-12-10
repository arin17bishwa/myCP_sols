import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    ArrayList<Integer> findTwoElement(int[] arr) {
        Map<Integer, Integer> freq = new HashMap<>();
        int n = arr.length;
        for (int j : arr) {
            freq.put(j, freq.getOrDefault(j, 0) + 1);
        }
        ArrayList<Integer> ans = new ArrayList<>(List.of(-1, -1));

        for (int i = 1; i <= n; i++) {
            if (freq.getOrDefault(i, 0) == 2) ans.set(0, i);
            else if (freq.getOrDefault(i, 0) == 0) ans.set(1, i);
        }

        return ans;
    }

}
