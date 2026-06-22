class Solution {
    static ArrayList<Integer> getSum(int N) {
        ArrayList<Integer> arr=new ArrayList<>();
        int esum=0;
        int osum=0;
        for(int i=1;i<=N;i++){
            if(i%2==0){
                esum+=i;
            }
            else{
                osum+=i;
            }
        }
        arr.add(esum);
        arr.add(osum);
        return arr;
    }
}