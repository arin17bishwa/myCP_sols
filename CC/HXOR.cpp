//
// Created by bishwajit on 13/12/20.
//

//NOT DONE(BUT PYPY ONE IS DONE)

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

void solve()
{
    ll x,n,k,i=0;
    vector<ll> arr;
    cin>>n>>x;
    arr.resize(n);
    for(auto &it:arr){
        cin>>it;
    }
    for(k=x;(k>0)&&(i<n-1);k--){
        ll f=0;
        ll power=log(arr[i])/log(2);
        ll p=(1<<power);
        arr[i]^=p;
        for(int j=i+1;j<n;j++){
            if((arr[j]^p)<arr[j]) {
                arr[j] ^= p;
                f = 1;
                break;
            }
        }

        if(f==0)
            arr[n-1]^=p;
        while(arr[i]<=0)
            i++;

    ll m=k;
    if((m>0)&&(n<3)&&((m&1)==0)){
        arr[n-1]^=1;
        arr[n-2]^=1;
    }


    }

    for(i=0;i<n;i++)
        cout<<arr[i]<<' ';
    cout<<"\n";

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
