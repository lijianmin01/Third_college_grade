#include <string.h>
#include <math.h>
#include<stdio.h>
int la(int a,int b){
    int c=0;
    while(c=a%b){
		a=b;
		b=c;
	}
    return b;
}

int main(void){
    int a,b,c,d,fm,fz,fz1,fz2,t,max;
    char arr[10000];
    while(scanf("%s",&arr)!=EOF){
        t=1;
        a=arr[0]-'0';b=arr[2]-'0';
        c=arr[4]-'0';d=arr[6]-'0';
        fm=b*d;
        fz1=a*d;
        fz2=b*c;
        if(arr[3]=='+') fz=fz1+fz2;
        if(arr[3]=='-'){
            if(fz1<fz2) {
                t=-1*t;
                fz=fz2-fz1;
            }
            else fz=fz1-fz2;
        }
        if(fz==0) printf("%d\n",0);
        else if(fz==fm) printf("%d\n",1*t);
        else if(fz<fm){
            max=la(fz,fm);
            fz/=max;
            fm/=max;
            printf("%d/%d\n",fz*t,fm);
        }
        else if(fz>fm){
            max=la(fm,fz);
            fz/=max;
            fm/=max;
            if(fm==1) printf("%d\n",fz*t);
            else printf("%d/%d\n",fz*t,fm);
        }
    }
    return 0;
}