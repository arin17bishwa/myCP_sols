#include <iostream>
#include <cstdio>
#include <bits/stdc++.h>
using namespace std;

int func(int n){
    string answer;
    if(n<=9){
        if (n==1)answer = "one";
        else if (n==2)answer="two";
        else if (n==3)answer="three";
        else if (n==4)answer="four";
        else if (n==5)answer="five";
        else if (n==6)answer="six";
        else if (n==7)answer="seven";
        else if (n==8)answer="eight";
        else if (n==9)answer="nine";
    }
    else {
        if(n&1)answer="odd";
        else answer="even";
    }
    cout<<answer<<endl;
    return 0;
}


int main() {
    // Complete the code.
    int a,b;
    cin>>a>>b;
    for(int i=a;i<=b;i++){
        func(i);
    }
    return 0;
}