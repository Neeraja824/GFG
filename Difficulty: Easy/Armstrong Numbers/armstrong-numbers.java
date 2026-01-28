// User function Template for Java
class Solution {
    static boolean armstrongNumber(int n) {
        // code here
        int num=n;
        int sum=0;
        while(n!=0){
            int l=n%10;
            sum+=(l*l*l);
            n/=10;
        }
        return num==sum;
    }
}