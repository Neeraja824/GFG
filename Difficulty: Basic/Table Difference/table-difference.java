// User function Template for Java
class Solution {
    public static void difference(int n1, int n2) {

        // Write your code here
        int n=Math.abs(n1-n2);
        for(int i=1;i<11;i++){
            System.out.print(n*i+" ");
        }
    }
}