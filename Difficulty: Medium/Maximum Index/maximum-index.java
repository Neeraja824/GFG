class Solution {
    int maxIndexDiff(int[] arr) {
        int n=arr.length;
        int res=0;
        Stack<Integer> st=new Stack<>();
        
        for(int i=0;i<n;i++){
            if(st.isEmpty() || arr[st.peek()]>=arr[i]){
                st.push(i);
            }
        }
        
        for(int i=n-1;i>=0;i--){
            while(!st.isEmpty() && arr[i]>=arr[st.peek()]){
                int ind=st.pop();
                res=Math.max(res,i-ind);
            }
        }
        
        return res;
    }
}