package Leetcode

func maximumTripletValue(nums []int) int64 {
	n := len(nums)
	var ans int64 = 0
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			for k := j + 1; k < n; k++ {
				ans = max(ans, int64((nums[i]-nums[j])*nums[k]))
			}
		}
	}
	return ans
}
