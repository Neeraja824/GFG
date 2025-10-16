#User function Template for python3
arr = tuple(map(int, input().split()))
for i in arr:
    if(arr.count(i)>1):
        print(False)
        break
else:
    print(True)
########### Write your code below ###############
# Print "True" if all elements of tuple are different, otherwise print "False"

########### Write your code above ###############