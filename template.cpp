#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define endl '\n'
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
    cout<<"hello world";
}


int main()
{
    file_IO();
    int T = 1;
    //cin >> T;
    while (T--)
    {
        solve();
    }
}



/*
void build(ll node,ll l,ll r) {
    //cout<<l<<' '<<r;
    if (l == r) {
        tree[node] = arr[l];
        return;
    }
    ll mid = (l + r) / 2;
    build((node << 1) | 1, l, mid);
    build((node << 1 )+ 2, mid + 1, r);
    tree[node]=tree[node<<1|1]+tree[(node<<1)+2];
}

ll query(int node,int l,int r,int L,int R){
    if(r<L || l>R){
        return 0;
    }
    if(l>=L && r<=R){
        return tree[node];
    }
    int mid=(l+r)/2;
    ll left = query((node<<1)|1,l,mid,L,R);
    ll right = query((node<<1)+2,mid+1,r,L,R);
    return left+right;
}

void point_update(int node,int l, int r,int ind,ll val){
    if(ind<l || r<ind)
        return;
    if (ind>=r && ind<=l){
        tree[node]=val;
        return;
    }
    int mid=(l+r)/2;
    point_update((node<<1)|1,l,mid,ind,val);
    point_update((node<<1)+2,mid+1,r,ind,val);
    tree[node]=tree[node<<1|1]+tree[(node<<1)+2];
}
*/