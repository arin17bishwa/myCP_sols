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

ll func(ll n){
    ll high,low,mid;
    high=1000000000;
    low=1;
    mid=1;
    while (low<=high){
        mid = low + (high - low) / 2;
        if (((mid * (mid + 1)) / 2) > n)
            high=mid-1;
        else if (((mid * (mid + 1)) / 2) <n)
            low=mid+1;
        else
            return mid;
    }

    if(((mid * (mid + 1)) / 2) <n)
        return mid+1;
    return mid;
}

void solve(){
    ll n;
    cin >> n;
    cout <<func(n)<<endl;

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