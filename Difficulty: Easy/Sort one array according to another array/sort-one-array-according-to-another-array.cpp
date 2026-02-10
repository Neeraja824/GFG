// User function Template for C++

void sortArray(int a[], char b[], int n) {
    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-i-1;j++){
            if(a[j]>a[j+1]){
                int temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
                char t=b[j];
                b[j]=b[j+1];
                b[j+1]=t;
            }
        }
    }
}
