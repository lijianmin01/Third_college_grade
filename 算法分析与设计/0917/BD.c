/*
a×((a×a-a+1))+2×a(a-1)/2
=a×a×a-a×a+a+a×a-a
=a×a×a
定理成立。证毕。
通过定理的证明过程可知L所要求的奇数数列的首项为(a×a-a+1)，长度为a。
*/
#include<stdio.h>

int main(){
    int n,f,i;
    scanf("%d",&n);
    f=(n*n-n+1);
    printf("%d*%d*%d=%d=",n,n,n,n*n*n);
    for ( i = 0; i < n; i++)
    {
        printf("%d",f);
        if(i+1!=n){
            printf("+");
        }
        f+=2;
    }
    
    return 0;
}