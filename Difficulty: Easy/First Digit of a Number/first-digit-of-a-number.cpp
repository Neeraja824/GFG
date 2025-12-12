int firstDigit(int n) {
    // code here
    int ans;
    while(n>0){
        ans=n%10;
        n=n/10;
    }
    return ans;
}