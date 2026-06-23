class Solution {
    public static int maximumElement(ArrayList<Integer> arr) {
        // code here
        arr.sort(null);
        return arr.getLast();
    }

    public static int minimumElement(ArrayList<Integer> arr) {
        // code here.
        arr.sort(null);
        return arr.getFirst();
    }
}
