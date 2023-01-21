//
// Created by bishwajit on 17/12/20.
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
using tapatap=tuple<ll,int,int>;

vector<tapatap> arr;

void solve()
{
    int a,b;
    cin>>a>>b;
    auto ans=*upper_bound(arr.begin(),arr.end(),tapatap(a*a+b*b,INT_MAX,INT_MAX));

    cout<<get<1>(ans)<<' '<<get<2>(ans)<<"\n";
}


int main()
{
    file_IO();
    int T = 1;
    arr.resize(4000000);
    int k=0;
    for(int i = 0;i<2000;i++){
        for(int j = 0;j<2000;j++,k++)
            arr[k]=tapatap(i*i+j*j,i,j);
    }
    sort(arr.begin(),arr.end());
    cin >> T;
    while (T--)
    {
        solve();
    }
}



