#include<stdio.h>

int main(){
    int N[10005];
    int i,j,T,n,cnt;
    scanf("%d",&T);
    while (T--)
    {
        scanf("%d",&n);
        for ( i = 0; i < n; i++)
        {
            scanf("%d",&N[i]);
        }

        for ( i = 0; i < n-1; i++)
        {
            for ( j = 0; j < n-i-1; j++)
            {
                if(N[j]>N[j+1]){
                    cnt = N[j+1];
                    N[j+1] = N[j];
                    N[j] = cnt;
                }
            }
            
        }
        int sum=0;
        //剩余人数
        int p_nums = n;
        int a,b,c,d; 
        while(p_nums>3){
            a = N[0];
            b = N[1];
            c = N[p_nums-2];
            d = N[p_nums-1];

            int f1=0,f2=0;
            f1 = c+a+d+a;
            f2 = b+a+d+b;
            if(f1<f2){
                sum+=f1;
            }else{
                sum+=f2;
            }
            p_nums -= 2;
        }

        if(p_nums==1){
            sum+=N[0];
        }
        if(p_nums==2){
            sum+=N[1];
        }

        if(p_nums==3){
            sum+=N[0]+N[1]+N[2];
        }
        printf("%d\n",sum);
    }
    
    return 0;
}