package Leetcode

import "strings"

func bestClosingTime(customers string) int {
	n := len(customers)
	total_customers := strings.Count(customers, "Y")
	min_penalty := total_customers
	ans := 0
	current_customers := 0
	if customers[0] == 'Y' {
		current_customers = 1
	}

	for i := 1; i < n; i++ {
		curr_penalty := (i - current_customers) + (total_customers - current_customers)
		if curr_penalty < min_penalty {
			min_penalty = curr_penalty
			ans = i
		}
		if customers[i] == 'Y' {
			current_customers++
		}
	}

	if min_penalty <= (n - total_customers) {
		return ans
	}
	return n

}
