// User function Template for C++

void square(int s) {
    for(int i=1;i<=s;i++){
        for(int j=1;j<=s;j++){
            if(i==1 or i==s or j==1 or j==s)cout<<"* ";
            else cout<<"  ";
            
        }
        cout<<endl;
    }
}
