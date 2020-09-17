#include<stdio.h>
int nums[10];
void one(int nums[10]){
    int i;
    for(i=0;i<10;i++){
        scanf("%d",&nums[i]);
    }
}

void two(int nums[10]){
    int max,min,max_i,min_i;
    max_i=0;
    min_i=0;
    max=nums[0];
    min=nums[0];

    int i;
    for(i=0;i<10;i++){
        if(max<nums[i]){
            max = nums[i];
            max_i=i;
        }
        if(min>nums[i]){
            min = nums[i];
            min_i = i;
        }
    }
    int cnt;
    
    if (max_i == 0 && min_i==9){
    	//最大的数在第一个位置，最小的数在最后这样就很难排序啦！
    	nums[0]=min;
    	nums[9]=max;
	}else{
		cnt=nums[0];
	    nums[0]=min;
	    nums[min_i]=cnt;
	
	    cnt=nums[9];
	    nums[9]=max;
	    nums[max_i]=cnt;
	}
    

}
void three(int nums[10]){
    int i;
    for ( i = 0; i < 10; i++)
    {
        printf("%d ",nums[i]);
    }
    
}
int main(){
    one(nums);
    two(nums);
    three(nums);
    return 0;
}