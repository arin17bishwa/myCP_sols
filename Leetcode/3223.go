package Leetcode

func minimumLength(s string) int {
	counter := make(map[rune]int)
	for _, ch := range s {
		counter[ch]++
	}
	ans := 0
	for _, count := range counter {
		if count&1 != 0 {
			ans++
		} else {
			ans += 2
		}
	}
	return ans
}
