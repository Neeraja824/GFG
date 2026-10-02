class Solution:
	def findSum(self, s1, s2):
		# code here
        result = []
        carry = 0
        i = len(s1) - 1
        j = len(s2) - 1
        while i >= 0 or j >= 0 or carry:
            digit1 = int(s1[i]) if i >= 0 else 0
            digit2 = int(s2[j]) if j >= 0 else 0
            total = digit1 + digit2 + carry
            carry = total // 10
            current_digit = total % 10
            result.append(str(current_digit))
            i -= 1
            j -= 1
        ans = "".join(result[::-1])
        ans = ans.lstrip('0')
        return ans if ans else "0"