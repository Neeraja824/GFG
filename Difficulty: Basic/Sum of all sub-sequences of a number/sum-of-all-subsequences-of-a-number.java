class Solution {
    int subsequenceSum(String s) {
        int n = s.length();
        int p = (int)Math.pow(2, n - 1);
        int sum = 0;

        for (int i = 0; i < n; i++) {
            sum += p * (s.charAt(i) - '0');
        }

        return sum;
    }
}
