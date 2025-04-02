package Leetcode

func maximumTripletValue(nums []int) int64 {
	n := len(nums)
	var ans int64 = 0
	prefixMax := append(make([]int, 0), nums...)
	suffixMax := append(make([]int, 0), nums...)

	for i := 1; i < n; i++ {
		prefixMax[i] = max(prefixMax[i-1], prefixMax[i])
	}
	for i := n - 2; i > -1; i-- {
		suffixMax[i] = max(suffixMax[i], suffixMax[i+1])
	}

	for j := 1; j < n-1; j++ {
		ans = max(ans, int64((prefixMax[j-1]-nums[j])*suffixMax[j+1]))
	}

	return ans
}
