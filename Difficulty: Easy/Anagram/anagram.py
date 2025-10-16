class Solution:
    def areAnagrams(self, s1, s2):
       # code here
       val1=sorted(s1)
       val2=sorted(s2)
       if len(val1)==len(val2) and val1==val2:
           return True
       else:
           return False
       