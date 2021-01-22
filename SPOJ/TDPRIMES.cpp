//
// Created by bishwajit on 07/01/21.
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
ll const MAX=100000001;


void solve()
{
    vector<bool> arr;
    vector<ll> primes;
    arr.resize(MAX,true);
    primes.reserve(60000000);
    arr[0]=arr[1]=false;

    for(ll i=2;i<=MAX;i++){
        if(arr[i]){
            primes.emplace_back(i);
            for(ll j=i*i;j<=MAX;j+=i)
                arr[j]=false;
        }
    }

    ll n=primes.size();
    for(ll i=0;i<n;i+=100)
        cout<<primes[i]<<endl;
}


int main()
{
    //file_IO();
    int T = 1;
    //cin >> T;
    while (T--)
    {
        solve();
    }
}

