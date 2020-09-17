#include<stdio.h>

int main(){
    int n;
    int AH,AM,AS,BH,BM,BS;
    int h,m,s,cnt;
    while(n--){
        scanf("%d %d %d %d %d %d",&AH,&AM,&AS,&BH,&BM,&BS);
        cnt = (AS+BS)/60;
        s = (AS+BS)%60;

        m = (AM+BM+cnt)%60;
        cnt = (AM+BM+cnt)/60;

        h = AH+BH+cnt;
        printf("%d %d %d\n",h,m,s);
        
    }
    return 0;
}