//
// Created by bishwajit on 07/12/20.
//

#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
    ll n,a,b,c;
    vector<ll> vec;
    cin >> n;
    vec.resize(n);
    for(auto &it : vec){
        cin >> it;
    }

    cin >>a;
    vec.erase(vec.begin()+a-1);
    cin >> b>>c;
    vec.erase(vec.begin()+b-1,vec.begin()+c-1);
    cout << vec.size()<<'\n';

    for (auto it: vec){
        cout << it<<' ';
    }
    return 0;
}