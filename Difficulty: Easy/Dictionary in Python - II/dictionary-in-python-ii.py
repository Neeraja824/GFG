def pair_sum(arr, sum):
    # code here
    for i in range(0,len(arr)):
        for j in range(1,len(arr)):
            if arr[i]+arr[j]==sum:
                return True
    return False