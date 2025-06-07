package Leetcode

import "sort"

func findEvenNumbers(digits []int) []int {
	candidates := make(map[int]int)
	for i, d1 := range digits {
		if d1 == 0 {
			continue
		}
		for j, d2 := range digits {
			if i == j {
				continue
			}
			for k, d3 := range digits {
				if k == i || k == j {
					continue
				}
				if d3&1 != 0 {
					continue
				}
				candidates[d1*100+d2*10+d3] = 1
			}
		}
	}
	ans := make([]int, 0)
	for k, _ := range candidates {
		ans = append(ans, k)
	}
	sort.Ints(ans)
	return ans
}
