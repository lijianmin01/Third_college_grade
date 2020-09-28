#include <string.h>
#include <stdio.h>
struct student
{
	char  num[6];
	char name[20];
	int score[3];
}stu[100];

int main(){
    int i, j ,n,m;
    int a=0,b=0,c=0,max;
    scanf("%d",&n);
    //记录数据
	for(i=0;i<n;i++){
		scanf("%s",stu[i].num);
		scanf("%s",stu[i].name);
		for(j=0;j<3;j++){
			scanf("%d",&stu[i].score[j]);
		}
	}
	//汇总数据
	m=0;max=0;
    for(i=0;i<n;i++){
        a+=stu[i].score[0];
        b+=stu[i].score[1];
        c+=stu[i].score[2];
        if(max<(stu[i].score[0]+stu[i].score[1]+stu[i].score[2])) {
            max=stu[i].score[0]+stu[i].score[1]+stu[i].score[2];
            m=i;
        }
    }
    printf("%d %d %d\n",a/n,b/n,c/n);
    printf("%s %s %d %d %d \n",stu[m].num,stu[m].name,stu[m].score[0],stu[m].score[1],stu[m].score[2]);
	return 0;
}