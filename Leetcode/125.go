package Leetcode

import (
	"unicode"
)

func isPalindrome(s string) bool {
	n := len(s)

	for head, tail := 0, n-1; head < tail; {
		for head < tail && !isAlphaNumeric(rune(s[head])) {
			head++
		}
		for head < tail && !isAlphaNumeric(rune(s[tail])) {
			tail--
		}
		if head == tail {
			return true
		}
		if unicode.ToLower(rune(s[head])) != unicode.ToLower(rune(s[tail])) {
			return false
		}
		head++
		tail--
	}
	return true
}

func isAlphaNumeric(ch rune) bool {
	return unicode.IsDigit(ch) || unicode.IsLetter(ch)
}
