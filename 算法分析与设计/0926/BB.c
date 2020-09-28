#include<stdio.h>
#include<string.h>

int main() {
    int n,n1,n2;
    scanf("%d",&n);
    if(n==0){
        return 0;
    }
    n1=n;
    n2=n;
    char sno[20];
    char name[20];
    int a,b,c;

    int sum1=0,sum2=0,sum3=0,cnt=0;

    char sno1[20];
    char name1[20];
    int a1,b1,c1;
    int big_cnt=1;
	
    scanf("%s %s %d %d %d",sno,name,&a,&b,&c);
    
    //printf("%s %s %d %d %d\n",sno,name,a,b,c);

    strcpy(sno1,sno);
    strcpy(name1,name);
    a1=a;
    b1=b;
    c1=c;

    sum1=a;
    sum2=b;
    sum3=c;

    cnt =a+b+c;
    n1--;
    while(n1--){
        scanf("%s %s %d %d %d",sno,name,&a,&b,&c);

        sum1+=a;
        sum2+=b;
        sum3+=c;

        if(cnt<(a+b+c)){
            strcpy(sno1,sno);
            strcpy(name1,name);
            a1=a;
            b1=b;
            c1=c;
            big_cnt=1;
        }   big_cnt++;
        
    }
    printf("%d %d %d\n",sum1/n2,sum2/n2,sum3/n2);
    
	printf("%s %s %d %d %d \n",sno1,name1,a1,b1,c1);

    getchar();
    return 0;
}
