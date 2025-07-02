package Leetcode

func maxAdjacentDistance(nums []int) int {
	ans := 0
	n := len(nums)
	for i := range n - 1 {
		ans = max(ans, abs(nums[i+1]-nums[i]))
	}
	return max(ans, abs(nums[n-1]-nums[0]))
}

func abs(a int) int {
	if a > 0 {
		return a
	} else {
		return -a
	}
}
