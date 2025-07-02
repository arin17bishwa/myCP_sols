package Leetcode

func lexicalOrder(n int) []int {
	ans := make([]int, 0)

	for startDigit := 1; startDigit < 10; startDigit++ {
		if len(ans) > n {
			break
		}
		dfsLexicalOrder(startDigit, n, &ans)
	}
	return ans
}

func dfsLexicalOrder(curr, limit int, ans *[]int) {
	if curr > limit {
		return
	}
	*ans = append(*ans, curr)
	if curr*10 > limit {
		return
	}

	for i := range 10 {
		dfsLexicalOrder(curr*10+i, limit, ans)
	}

}
