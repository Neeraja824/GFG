class Solution {
    public int reverseExponentiation(int n) {
        // code here
        int rev=0;
        int temp=n;
        while(temp>0){
            int ld=temp%10;
            rev+=ld;
            temp/=10;
        }
        return (int)Math.pow(n,rev);
    }
}
