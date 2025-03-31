package Leetcode

import (
	"strings"
)

func isPalindrome(s string) bool {
	n := len(s)

	for head, tail := 0, n-1; head < tail; {
		for head < tail && !isAlphaNumeric(s[head]) {
			head++
		}
		for head < tail && !isAlphaNumeric(s[tail]) {
			tail--
		}
		if head == tail {
			return true
		}
		if strings.ToLower(string(s[head])) != strings.ToLower(string(s[tail])) {
			return false
		}
		head++
		tail--
	}
	return true
}

func isAlphaNumeric(ch uint8) bool {
	return (ch >= 48 && ch <= 57) || (ch >= 65 && ch <= 90) || (ch >= 97 && ch <= 122)
}
