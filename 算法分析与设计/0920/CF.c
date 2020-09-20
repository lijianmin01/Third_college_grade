#include<stdio.h>

int main(){
    int V,D;
    scanf("%d %d",&V,&D);

    int count;
    if(V%D==0){
        count=V/D;
    }else{
        count==V/D+1;
    }

    int time=count;
    int nums=count;
    int cnt=1;
    while(nums){
        nums-=cnt;
        cnt+=2;
        time++;
        if(nums<=cnt){
            break;
        }
    }
    printf("%d\n",time);

    return 0;
}