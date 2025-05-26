package Leetcode

type NumArray struct {
	prefixSum []int
}

func Constructor(nums []int) NumArray {
	n := len(nums)
	prefixSum := make([]int, n+1)
	for i := 1; i <= n; i++ {
		prefixSum[i] = prefixSum[i-1] + nums[i-1]
	}
	return NumArray{
		prefixSum: prefixSum,
	}
}

func (this *NumArray) SumRange(left int, right int) int {
	return this.prefixSum[right+1] - this.prefixSum[left]
}

/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.SumRange(left,right);
 */
