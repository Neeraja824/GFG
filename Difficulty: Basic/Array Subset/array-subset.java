
class Solution {
    public boolean isSubset(int a[], int b[]) {
        // Your code here
        int [] f=new int[1000001];
        for(int i=0;i<a.length;i++){
            f[a[i]]++;
        }
        for(int j=0;j<b.length;j++){
            if(f[b[j]]==0){
                return false;
            }
            f[b[j]]--;
        }
        return true;
    }
}
