#include <iostream>
#include <cstdio>
#include <bits/stdc++.h>
using namespace std;

int func(int k,) {
    string answer;
    if(k <= 9){
        if (k == 1)answer = "one";
        else if (k == 2)answer="two";
        else if (k == 3)answer="three";
        else if (k == 4)answer="four";
        else if (k == 5)answer="five";
        else if (k == 6)answer="six";
        else if (k == 7)answer="seven";
        else if (k == 8)answer="eight";
        else if (k == 9)answer="nine";
    }
    else {
        if(k & 1)answer="odd";
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
        func(i, 0);
    }
    return 0;
}