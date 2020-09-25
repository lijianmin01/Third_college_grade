#include<stdio.h>

int count;
int nums[30];
int maxcount;


void pandu(int max,int index,int daodan){
    if(index==count){
    	//printf("%d %d\n",index,daodan);
        if(daodan>maxcount){
            maxcount=daodan;
        }
    }else{
        int i;
        for ( i = index; i < count; i++)
        {
            if(nums[i]<=max){
                daodan++;
                //printf("%d\n",daodan);
                max=nums[i];
                pandu(max,i+1,daodan);
	            if(daodan>maxcount){
		            maxcount=daodan;
		        }
            }
        }
        
    }
}

int main(){
    int flag=7;
    while(scanf("%d",&nums[count++])!=EOF){
        if(count>=7){
            break;
        }
    }

    int cnt;int index;int daodan,i;
    int max;
	maxcount=1;
    for ( i = 0; i < count; i++)
    {
        max=nums[i];
        index=i;
        daodan=1;
        pandu(max,i+1,daodan);
        
    }
    
    printf("%d\n",maxcount+1);


    return 0;
}