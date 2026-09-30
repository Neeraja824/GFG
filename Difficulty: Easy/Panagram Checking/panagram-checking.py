class Solution:
    def checkPangram(self,s):
        #code here
        res=[]
        for i in s:
            if i.isalpha():
                res.append(i.lower())
        return len(set(res))==26