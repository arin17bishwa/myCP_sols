package Leetcode

func answerString(word string, numFriends int) string {
	n := len(word)

	if n == 1 || numFriends == 1 {
		return word
	}

	if numFriends == n {
		return maxCharacter(word)
	}

	ans := ""

	for i := range n {
		ans = max(ans, word[i:min(n, i+(n-numFriends+1))])
	}
	return ans
}

func maxCharacter(word string) string {
	ans := ""
	for _, ch := range word {
		ans = max(ans, string(ch))
	}
	return ans
}
