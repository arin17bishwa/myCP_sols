//
// Created by bishwajit on 12/12/20.
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

//vector<int> adj[5005];
vector<vector<int>> arr;


ll func(int h,int w){
    ll ans = 0;
    vector<vector<ll>> dp;
    dp.resize(h);
    if(w==1){
        for(int i=0;i<h;i++){
            ans+=arr[i][0];
        }
        return ans;
    }
    for(int j=0;j<w;j++){
        dp[0].push_back(arr[0][j]);
    }
    for(int i=1;i<h;i++){
        dp[i].resize(w);
        for(int j=0;j<w;j++){
            if(j==0){
                dp[i][j] = arr[i][j] + max(dp[i - 1][j], dp[i - 1][j + 1]);
            }
            else if(j==w-1){
                dp[i][j] = arr[i][j] + max(dp[i - 1][j], dp[i - 1][j - 1]);
            }
            else {
                dp[i][j] = arr[i][j] + max(max(dp[i - 1][j - 1], dp[i - 1][j]), dp[i - 1][j + 1]);
            }
        }
    }
    return *max_element(dp[h-1].begin(),dp[h-1].end());

}

void solve()
{
    int h,w;
    cin>>h>>w;
    arr.resize(h);
    for(int i=0;i<h;i++){
        arr[i].resize(w);
        for(int j=0;j<w;j++){
            cin>>arr[i][j];
        }
    }

    ll ans=func(h,w);
    cout<<ans<<"\n";
}


int main()
{
    file_IO();
    int T = 1;
    cin >> T;
    while (T--)
    {
        solve();
    }
}
