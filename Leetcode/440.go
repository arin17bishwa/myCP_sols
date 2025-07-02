package Leetcode

func findKthNumber(n int, k int) int {
	curr := 1
	k--

	for {
		if k <= 0 {
			break
		}
		steps := countSteps(n, curr)

		if steps > k {
			curr *= 10
			k--
		} else {
			curr++
			k -= steps
		}
	}

	return curr

}

func countSteps(n, curr int) int {
	steps := 0
	nxt := curr + 1

	for {
		if curr > n {
			break
		}
		steps += min(n+1, nxt) - curr
		curr *= 10
		nxt *= 10
	}

	return steps
}
