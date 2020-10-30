#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    vector<vector<int>> vec;
    int n,k,q,a,b,x;
    cin >> n>>q;
    for(int i=0;i<n;i++){
        cin >> k;
        int arr[k];
        vector<int> temp;
        for (int j=0;j<k;j++){
            cin >> x;
            temp.push_back(x);
        }
        vec.push_back(temp);
    }
    while(q--){
        cin >> a>>b;
        cout << vec[a][b]<<endl;
    }

    return 0;
}