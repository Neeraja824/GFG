// User function Template for Java

class Solution {
    static int countSquares(int n) {
        // code here
        int res=(int)Math.sqrt(n);
        if(res*res==n){
            return res-1;
        }
        return res;
    }
}