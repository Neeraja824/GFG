class Solution {
    static int inSequence(int a, int b, int c) {
        int ans = 0;
        for(int i =1; i>=1; i++){
            
            int an = 0;
             an = a+i*c;
            if(an<=b){
                if(an==b){
                    ans =  1;
                    break;
                }
            }
            else{
                ans = 0;
                break;
            }
            
        }
        return ans;
    }
}