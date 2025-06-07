package Leetcode

import "math"

func countGoodTriplets(arr []int, a int, b int, c int) int {
	ans := 0
	n := len(arr)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if math.Abs(float64(arr[i]-arr[j])) > float64(a) {
				continue
			}
			for k := j + 1; k < n; k++ {
				if math.Abs(float64(arr[j]-arr[k])) > float64(b) || math.Abs(float64(arr[i]-arr[k])) > float64(c) {
					continue
				} else {
					ans++
				}
			}
		}
	}
	return ans

}
