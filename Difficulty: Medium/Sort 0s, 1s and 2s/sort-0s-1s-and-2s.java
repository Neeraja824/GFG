class Solution {
    public void sort012(int[] arr) {
        int low = 0, mid = 0, high = arr.length - 1, c;

        while (mid <= high) {
            if (arr[mid] == 0) {
                c = arr[low];
                arr[low] = arr[mid];
                arr[mid] = c;
                low++;
                mid++;
            } else if (arr[mid] == 1) {
                mid++;
            } else {
                c = arr[mid];
                arr[mid] = arr[high];
                arr[high] = c;
                high--;
            }
        }
    }
}
