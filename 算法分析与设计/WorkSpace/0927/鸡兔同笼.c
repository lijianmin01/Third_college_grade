#include<stdio.h>

int main(){
    int count,n,m;
    int x,y;
    scanf("%d",&count);
    while (count--)
    {
        scanf("%d %d",&n,&m);
        x = (4*n-m)/2;
        y = (m-2*n)/2;
        if((4*n-m)%2!=0){
            printf("No answer\n");
        }else if(x<0 || y<0){
            printf("No answer\n");
        }
        else{
            
            printf("%d %d\n",x,y);
        }
    }
    
    return 0;
}