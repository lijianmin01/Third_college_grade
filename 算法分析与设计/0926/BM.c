#include<stdio.h>

void f(){
    int a,b;
    scanf("%d %d",&a,&b);
    int hangshu=a*b-b+1;
    int kongge=0;
    int i,j;
    int flag = -1;
    while(hangshu--){
        for(i=0;i<kongge;i++){
            printf(" ");
        }
        printf("X");
        if((kongge+1)==(a+1)/2){

        }else{
            for(j=0;j<a-2-kongge*2;j++){
                printf(" ");
            }
            printf("X");
        }
        printf("\n");
        if(flag==-1){
        	kongge++;
        	if(kongge==(a+1)/2){
	            kongge-=2;
	            flag*=(-1);
        	}
		}else{
			kongge--;
			if(kongge==-1){
				kongge=1;
				flag*=(-1);
			}
		}
        
    }
    printf("\n");
}

int main(){
    int n;
    scanf("%d",&n);
    while (n--){
        f();
    }
    return 0;
}