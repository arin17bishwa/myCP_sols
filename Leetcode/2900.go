package Leetcode

func getLongestSubsequence(words []string, groups []int) []string {
	n := len(words)
	ans := make([]string, 0, n)
	last := -1
	for idx, word := range words {
		if groups[idx] != last {
			last = groups[idx]
			ans = append(ans, word)
		}
	}
	return ans
}
