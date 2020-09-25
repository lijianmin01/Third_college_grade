#include<stdio.h>
int main (void){
    int N, i, j;
    scanf("%d",&N);
    int arr[6];
    if (N>=1 && N<=100) {
        for (i = 0; i < N; i++) {

            for (j = 0; j < 6; j++) {
                int num;
                scanf("%d",&num);
                if (num>=0 && num<=15) {
                    arr[j] = num;
                }
            }
            
            if (arr[1] == arr[3] && arr[3] == arr[5]) {
                printf("Can not form a triangle.");
            }
            else if ((arr[0]-arr[2])/(arr[1]-arr[3]) == (arr[2]-arr[4])/(arr[3]-arr[5])) {
                printf("Can not form a triangle.");
            }
            else {
                int a, b, c;
                a = sqrt(pow(arr[0]-arr[2])+pow(arr[1]-arr[3]));
                b = sqrt(pow(arr[0]-arr[4])+pow(arr[1]-arr[5]));
                c = sqrt(pow(arr[4]-arr[2])+pow(arr[5]-arr[3]));
                int p = (a + b + c)/2;
                double S = sqrt(p*(p-a)*(p-b)*(p-c));
                printf("%.3f",S);
            }
        }
		}

    return 0;
}