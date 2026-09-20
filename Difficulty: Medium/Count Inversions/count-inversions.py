class Solution:
    def inversionCount(self, arr):
        # Code Here
        return self.mergeSort(arr, 0, len(arr)-1)

    def merge(self, arr, low, mid, high):

        temp = []
        left, right = low, mid + 1

        count = 0

        while left <= mid and right <= high:

            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                count += (mid - left + 1)
                right += 1

        # add remaining elements from left & right
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1

        # copy temp result to orogonal array
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

        return count


    def mergeSort(self, arr, low, high):

        total_count = 0

        if low >= high:
            return total_count

        mid = (low + high) // 2

        # collect count inversion from left & right half array
        total_count += self.mergeSort(arr, low, mid)
        total_count += self.mergeSort(arr, mid+1, high)

        total_count += self.merge(arr, low, mid, high)

        return total_count
