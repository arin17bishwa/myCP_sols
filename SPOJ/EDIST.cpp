//
// Created by bishwajit on 05/01/21.
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
    string a,b;
    cin>>a;
    cin>>b;
    int x=a.length();
    int y=b.length();
    int arr[y+1][x+1];
    for(int i=0;i<x+1;i++)
        arr[0][i]=i;
    for(int j=0;j<y+1;j++)
        arr[j][0]=j;

    for(int i=1;i<y+1;i++){
        for(int j=1;j<x+1;j++){
            if(a[j-1]==b[i-1])
                arr[i][j]=arr[i-1][j-1];
            else
                arr[i][j]=min(arr[i-1][j],min(arr[i-1][j-1],arr[i][j-1]))+1;
        }
    }
    cout<<arr[y][x]<<'\n';
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



