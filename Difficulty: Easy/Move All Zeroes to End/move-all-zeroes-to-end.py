class Solution:
	def pushZerosToEnd(self, arr):
    	# code here
    	n=len(arr)
    	i=0
    	for j in range(n):
    	    if(arr[j]):
    	        arr[i],arr[j]=arr[j],arr[i]
    	        i+=1