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

void file_IO()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}



//------- CODE STARTS HERE --------//


void solve()
{
    ll third,th_las,s,n,d,a;
    cin >>third>>th_las>>s;
    n=(s*2)/(third+th_las);
    d = (th_las - third) / (n - 5);
    a = third - (d*2);
    cout << n<<"\n";
    while(n--){
        cout<<a<<' ';
        a+=d;
    }
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



