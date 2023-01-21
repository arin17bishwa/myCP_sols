//
// Created by bishwajit on 06/12/20.
//

#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define sim template < class c
#define ris return * this
#define dor > debug & operator <<
#define eni(x) sim > typename \
  enable_if<sizeof dud<c>(0) x 1, debug&>::type operator<<(c i) {
sim > struct rge { c b, e; };
sim > rge<c> range(c i, c j) { return rge<c> {i, j}; }
sim > auto dud(c* x) -> decltype(cerr << *x, 0);
sim > char dud(...);
struct debug {
    ~debug() { cerr << endl; }
    eni( != ) cerr << boolalpha << i; ris;
    }
    eni( == ) ris << range(begin(i), end(i));
    }
    sim, class b dor(pair < b, c > d) {
        ris << "(" << d.first << ", " << d.second << ")";
    }
    sim dor(rge<c> d) {
        *this << "[";
        for (auto it = d.b; it != d.e; ++it)
            *this << ", " + 2 * (it == d.b) << *it;
        ris << "]";
    }
};
#define imie(...) " [" << #__VA_ARGS__ ": " << (__VA_ARGS__) << "] "
// debug & operator << (debug & dd, P p) { dd << "(" << p.x << ", " << p.y << ")"; return dd; }

void file_IO()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
/*
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
 */
}



//------- CODE STARTS HERE --------//


map<ll,ll> DP;
map<ll,ll> :: iterator it1;
vector<ll> vec;



ll func(int k,ll arr[]) {
    if(k==0)
        return 0;

    if(k==1){
        return arr[k];
    }
    it1=DP.find(k);
    if(it1==DP.end()){
        DP[k]=max(arr[k]*k+func(k-2,arr),func(k-1,arr));
    }
    return DP[k];

}

void solve()
{
    ll arr[100000+1]={0};
    int n;
    cin>>n;
    vec.resize(n);
    for(auto &iter:vec){
        cin>>iter;
        arr[iter]++;
    }
    cout<<func(100000, arr);

}


int main()
{
    file_IO();
    int T = 1;
    //cin >> T;
    DP[0]=0;
    while (T--)
    {
        solve();
    }
}
