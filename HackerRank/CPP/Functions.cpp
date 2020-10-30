#include <iostream>
#include <cstdio>
using namespace std;


int max_of_four(int a, int b,int c,int d){
    int arr[]={a,b,c,d};
    int m=-999999;
    for(int i : arr){
        if (i>m)m=i;
    }
    return m;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);

    return 0;
}