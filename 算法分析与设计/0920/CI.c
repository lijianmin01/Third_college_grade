#include<stdio.h>

int main(){
    int n;
    int t[1200];
    int d[1200];
    scanf("%d",&n);
    int i,j,cnt;
    while(n){
        for ( i = 0; i < n; i++)
        {
            scanf("%d",&t[i]);
        }
        for ( i = 0; i < n; i++)
        {
            scanf("%d",&d[i]);
        }

        for ( i = 0; i < n-1; i++)
        {
            for ( j = 0; j < n-i-j; j++)
            {
                if(t[j]>t[j+1]){
                    cnt = t[j];
                    t[j]=t[j+1];
                    t[j+1]=cnt;
                }

                if(d[j]>d[j+1]){
                    cnt = d[j];
                    d[j]=d[j+1];
                    d[j+1]=cnt;
                }
            }
        }
        
        int win=0;
        int index_d=0;
        for ( i = 0; i < n; i++)
        {
            if(t[i]>d[index_d]){
                win++;
                index_d++;
            }
            if(index_d==n){
                break;
            }
        }
        
        if(win>n/2){
            printf("YES\n");
        }else{
            printf("NO\n");
        }
        
        scanf("%d",&n);
    }
    return 0;
}