#include<stdio.h>

int main(){
    int years[100];
    int mons[100];
    int days[100];
    int i,j;
    int count=0;
    while(scanf("%d/%d/%d",&mons[count],&days[count],&years[count])!=EOF){
		count++;
    }
    int year,mon,day;

    for ( i = 0; i < count-1; i++)
    {
        for ( j = 0; j < count-i-1; j++)
        {
            if(years[j]>years[j+1]){
                year=years[j+1];
                years[j+1]=years[j];
                years[j]=year;

                mon=mons[j+1];
                mons[j+1]=mons[j];
                mons[j]=mon;

                day=days[j+1];
                days[j+1]=days[j];
                days[j]=day;
            }else if((years[j]==years[j+1])&&(mons[j]>mons[j+1])){
                mon=mons[j+1];
                mons[j+1]=mons[j];
                mons[j]=mon;

                day=days[j+1];
                days[j+1]=days[j];
                days[j]=day;
            }else if((years[j]==years[j+1])&&(mons[j]==mons[j+1])&&(days[j]>days[j+1])){
                day=days[j+1];
                days[j+1]=days[j];
                days[j]=day;
            }
        }
    }

    for ( i = 0; i < count ; i++)
    {
        printf("%02d/%02d/%d\n",mons[i],days[i],years[i]);
    }
    
    
    return 0;
}