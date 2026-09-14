class Solution:
    def alternateSort(self, arr):
        arr.sort()
        result = []
        left = 0
        right = len(arr) - 1
        while left <= right:
            result.append(arr[right])
            right -= 1

            if left <= right:
                result.append(arr[left])
                left += 1
        return result