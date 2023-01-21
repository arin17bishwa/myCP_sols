//
// Created by bishwajit on 07/12/20.
//


#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
    ll n,q,k,ind;
    vector<ll> vec;
    cin >> n;
    vec.resize(n);
    for(auto &it : vec){
        cin >> it;
    }
    cin >> q;
    while (q--){
        cin >> k;
        auto it=lower_bound(vec.begin(),vec.end(),k);
        ind=it-vec.begin();
        if(*it==k)
            cout<<"Yes";
        else
            cout<<"No";
        cout<<' '<<ind+1<<'\n';
    }
    return 0;
}