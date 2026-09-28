class Solution:
	def removeVowels(self, s):
		# code here
		stri = ""
		for ch in s:
		    if ch in "aeiou":
		       continue
		    stri += ch
        return stri
		