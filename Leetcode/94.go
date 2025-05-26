package Leetcode

// TreeNode Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorderTraversal(root *TreeNode) []int {
	ans := make([]int, 0)

	dfs(root, &ans)

	return ans
}

func dfs(node *TreeNode, curr *[]int) {

	if node == nil {
		return
	}

	dfs(node.Left, curr)
	*curr = append(*curr, node.Val)
	dfs(node.Right, curr)

}
