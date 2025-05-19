package Leetcode

import "sort"

func triangleType(nums []int) string {
	sort.Ints(nums)
	if nums[0]+nums[1] <= nums[2] {
		return "none"
	} else if nums[0] == nums[2] {
		return "equilateral"
	} else if nums[0] == nums[1] || nums[1] == nums[2] {
		return "isosceles"
	} else {
		return "scalene"
	}

}
