//
// Created by bishwajit on 07/12/20.
//

#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
    ll n;
    vector<ll> vec;
    cin >> n;
    vec.resize(n);
    for(auto &it : vec){
        cin >> it;
    }
    sort(vec.begin(),vec.end());
    for (auto it: vec){
        cout << it<<' ';
    }
    return 0;
}
