#User function Template for python3
n = int(input())
# Your code here
ans =True
for i in range(2,(n//2)+1):
    if n%i==0:
        ans=False
print(ans)
