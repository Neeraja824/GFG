class Solution:
    def concatenatedString(self,s1,s2):
        #code here
        set1=set(s1)
        set2=set(s2)
        chars=set1.intersection(s2)
        res1=[char for char in s1 if char not in chars]
        res2=[char for char in s2 if char not in chars]
        res=res1+res2
        if not res:
            return -1
        else:
            return "".join(res)