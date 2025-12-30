string conCat(string s1, string s2) {
    // code here.
    string s="";
    for(int i=0;i<s1.length();i++){
        s.push_back(s1[i]);
    }
    for(int j=0;j<s2.length();j++){
        s.push_back(s2[j]);
    }
    return s;
};
