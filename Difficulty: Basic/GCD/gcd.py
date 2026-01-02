#User function Template for python3
a = int(input())
b = int(input())

# Your code here
gcd=1
for i in range(1,100):
    if a%i==0 and b%i==0:
        gcd=i
print(gcd)
