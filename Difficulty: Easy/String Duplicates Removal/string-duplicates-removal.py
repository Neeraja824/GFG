class Solution:
	def removeDuplicates(self, s):
	    # code here
	    ans=""
	    for char in s:
	        if char not in ans:
	            ans+=char
	    return ans