void reverseString(char str[]) {
    // code here
    int len=strlen(str);
    for(int i=0;i<len/2;i++){
        char c=str[i];
        str[i]=str[len-i-1];
        str[len-i-1]=c;
    }
    printf("%s",str);
}