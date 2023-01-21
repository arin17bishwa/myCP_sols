#include <bits/stdc++.h>

using namespace std;



int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    // Write Your Code Here
    string answer;
    if (n==1)answer = "one";
    else if (n==2)answer="two";
    else if (n==3)answer="three";
    else if (n==4)answer="four";
    else if (n==5)answer="five";
    else if (n==6)answer="six";
    else if (n==7)answer="seven";
    else if (n==8)answer="eight";
    else if (n==9)answer="nine";
    else answer="Greater than 9";
    cout << answer;
    return 0;
}
