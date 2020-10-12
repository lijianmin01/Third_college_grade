import java.util.Scanner;

public class 逆序数 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

    }

    public static long mergeSort(int arr[]){
        int[] temp = new int[arr.length];
        return mergeSort(arr,temp,0,arr.length-1);
    }

    private static Long mergeSort(int[] arr,int[] temp,int start,int end){
        if(start>=end){
            return 0L;
        }
        int mid = start+(end-start)/2;  //避免溢出问题
        Long sum = mergeSort(arr, temp, start, mid);
        sum+=mergeSort(arr, temp, mid+1,end);
        sum+=merge(arr, temp, start,mid,end);
    }

    private static Long merge(int[] arr,int[] temp,int start,int mid,int end){
        Long sum=0L;
        int i = start,j=mid+1,k=start;
        while(i!=mid+1 && j!=end+1){
            if(arr[i]>arr[j]){
                temp[k++]=arr[j++];
                sum+=mid-i+1;
            }else{
                temp[k++]=arr[i++];
            }
        }

        while(i!=mid+1){
            temp[k++]=arr[i++];
        }
        while(j!=end){
            temp[k++]=arr[j++];
        }
    }
}
