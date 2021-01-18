#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
int a[10060],b[10060],k,n;
char c;
int main () {
    while (scanf("%d\n",&k) != EOF) {
        c=' ';
        n=0;
        b[0]=0;
        while (c != '\n' ) scanf("%d%c",&a[++n],&c);
        for (int i = 1; i <= n; i++)
            b[i]=a[i]+k*b[i-1];
        printf("q(x):");
        for (int i = 1; i < n; i++)
            printf(" %d",b[i]);
        printf("\nr = %d\n\n",b[n]);
    }
}