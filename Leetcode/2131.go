package Leetcode

func longestPalindrome(words []string) int {
	ans := 0
	singleExists := 0
	freq := make(map[string]int)
	for _, word := range words {
		freq[word]++
	}

	for word, cnt := range freq {
		palindrome := Reverse(word)
		if word == palindrome {
			ans += (cnt >> 1) << 2
			if cnt&1 != 0 {
				singleExists = 1
			}
		} else if palindromeCnt, ok := freq[palindrome]; word < palindrome && ok {
			ans += min(cnt, palindromeCnt) << 2
		}
	}
	return ans + (singleExists << 1)

}

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}
