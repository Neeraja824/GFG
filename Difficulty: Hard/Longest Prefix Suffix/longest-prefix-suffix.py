class Solution:
	def getLPSLength(self, s):
		# code here
		lps=[0]*len(s)
		length=0
		j=1
		while j<len(s):
		    if s[length]==s[j]:
		        length+=1
		        lps[j]=length
		        j+=1
		    else:
		        if length!=0:
		            length=lps[length-1]
		        else:
		            lps[j]=0
		            j+=1
		return lps[-1]