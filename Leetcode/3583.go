package Leetcode

const mod = int(1e9 + 7)

func specialTriplets(nums []int) int {
	ans := 0
	n := len(nums)
	prefixCounter := make(map[int]int)
	suffixCounter := make(map[int]int)

	for i := n - 1; i > 0; i-- {
		suffixCounter[nums[i]]++
	}

	prefixCounter[nums[0]]++

	for i := 1; i < n-1; i++ {
		suffixCounter[nums[i]]--
		ans = (ans + prefixCounter[nums[i]<<1]*suffixCounter[nums[i]<<1]) % mod
		prefixCounter[nums[i]]++
	}

	return ans

}
