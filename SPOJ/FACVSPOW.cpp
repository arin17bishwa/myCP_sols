//
// Created by bishwajit on 05/02/21.
//

#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define endl '\n'
#define maxn 10000001
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

vector<double> arr;

void solve()
{
    ll n,a,l,r,mid;
    double up,down;
    cin>>n;
    l=1;
    r=maxn+1;
    while(l<r){
        mid=(l+r)>>1;
        up=arr[mid];
        down=(double)mid*log(n);
        if(up>=down)
            r=mid;
        else
            l=mid+1;
    }

    cout<<l<<endl;
}


int main()
{
    file_IO();
    int T = 1;
    arr.resize(maxn+1,0);
    for(int i=1;i<=maxn;i++){
        arr[i]=arr[i-1]+log(i);
    }

    cin >> T;
    while (T--)
    {
        solve();
    }
}
