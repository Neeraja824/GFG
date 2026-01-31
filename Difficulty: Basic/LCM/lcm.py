#User function Template for python3
def LCM(a,b):
    # Your code here
    for i in range(max(a,b),a*b+1):
        if i%a==0 and i%b==0:
            return i