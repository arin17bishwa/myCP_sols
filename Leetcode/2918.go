package Leetcode

func minSum(nums1 []int, nums2 []int) int64 {
	s1, z1 := countingHelper(nums1)
	s2, z2 := countingHelper(nums2)

	if z1 == 0 && z2 == 0 {
		if s1 == s2 {
			return s1
		}
		return -1
	} else if z1 == 0 {
		if s1 >= s2+z2 {
			return s1
		}
		return -1
	} else if z2 == 0 {
		if s1+z1 <= s2 {
			return s2
		}
		return -1
	}
	return max(s1+z1, s2+z2)

}

func countingHelper(arr []int) (int64, int64) {
	sum, zero := 0, 0
	for _, n := range arr {
		sum += n
		if n == 0 {
			zero++
		}
	}
	return int64(sum), int64(zero)
}
