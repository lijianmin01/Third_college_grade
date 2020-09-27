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
    char sno[1];
    char name[6];
    int a,b,c;

    int sum1=0,sum2=0,sum3=0,cnt=0;

    char sno1[20][20];
    char name1[20][20];
    int a1[20],b1[20],c1[20];
    int big_cnt=1;
	
    scanf("%s %s %d %d %d",sno,name,&a,&b,&c);
    
    //printf("%s %s %d %d %d\n",sno,name,a,b,c);

    strcpy(sno1[0],sno);
    strcpy(name1[0],name);
    a1[0]=a;
    b1[0]=b;
    c1[0]=c;

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
            strcpy(sno1[0],sno);
            strcpy(name1[0],name);
            a1[0]=a;
            b1[0]=b;
            c1[0]=c;
            big_cnt=1;
        }else if(cnt==(a+b+c)){
        	strcpy(sno1[big_cnt],sno);
            strcpy(name1[big_cnt],name);
            a1[big_cnt]=a;
            b1[big_cnt]=b;
            c1[big_cnt]=c;
            big_cnt++;
		}
        
    }
    printf("%d %d %d\n",sum1/n2,sum2/n2,sum3/n2);
    int i;
    for(i=0;i<big_cnt;i++){
    	printf("%s %s %d %d %d\n",sno1[i],name1[i],a1[i],b1[i],c1[i]);
	}
    getchar();
    return 0;
}
