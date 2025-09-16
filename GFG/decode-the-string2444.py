class Solution:
    def decodedString(self, s):
        # code here
        stack = []
        curr_str = ""
        curr_digit = ""
        for i in range(len(s)):
            if s[i] == "[":
                stack.append(curr_str)
                stack.append(curr_digit)
                curr_digit = ""
                curr_str = ""
            elif s[i] == "]":
                prev_digit = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + curr_str * int(prev_digit)
            elif s[i].isdigit():
                curr_digit += s[i]
            else:
                curr_str += s[i]
        return curr_str
