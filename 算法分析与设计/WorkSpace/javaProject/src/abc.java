import java.lang.reflect.Array;
import java.util.Arrays;

public class abc {
    public static void main(String[] args) {
        int[] arr={3,0,10,2,9,1};
        insertSort(arr);
        System.out.println(Arrays.toString(arr));
    }

    //选择排序
    public static void selectionSort(int[] arr){
        int minIndex;
        for (int i = 0; i < arr.length-1; i++) {
            minIndex = i;
            for (int j = i+1; j <arr.length-i; j++) {
                if(arr[minIndex]>arr[j]){
                    minIndex=j;
//                    int temp = arr[i];
//                    arr[i]=arr[minIndex];
//                    arr[minIndex]=temp;
                }
            }
            int temp = arr[i];
            arr[i]=arr[minIndex];
            arr[minIndex]=temp;
//            arr[i] = arr[i]+arr[minIndex];
//            arr[minIndex] = arr[i]-arr[minIndex];
//            arr[i]=arr[i]-arr[minIndex];
        }
    }

    //选择排序 优化
    public static void selectionSort1(int[] arr){
        int minIndex,maxIndex;
        for (int i = 0; i < arr.length/2; i++) {
            minIndex = i;
            maxIndex = i;
            for (int j = i+1; j <arr.length-i; j++) {
                if(arr[minIndex]>arr[j]){
                    minIndex=j;
                }
                if(arr[maxIndex]<arr[j]){
                    maxIndex=j;
                }
            }
            int temp = arr[i];
            arr[i]=arr[minIndex];
            arr[minIndex]=temp;

            if(maxIndex==i){
                maxIndex=minIndex;
            }
            temp = arr[arr.length-i-1];
            arr[arr.length-i-1]=arr[maxIndex];
            arr[maxIndex]=temp;
        }
    }

    // 直接插入排序
    public static void insertSort(int[] arr){
        for (int i = 1; i < arr.length; i++) {
            int temp = arr[i];
            int j;
            for (j = i; j >0 && arr[j-1]>temp ; j--) {
                arr[j]=arr[j-1];
            }
            arr[j]=temp;
        }
    }

    //希尔排序
    public static void shellSort(int[] arr){
        for (int d = arr.length/2; d > 0  ; d/=2) {
            for (int i = d; i < arr.length ; i++) {
                int temp = arr[i];
                int j;
                for (j = i-d; j >=0 && temp < arr[j] ; j-=d) {
                    arr[j+d]=arr[i];
                }
                arr[j+d]=temp;
            }
        }
    }

    //归并排序
    public static void merge(int[] arr,int[] temp,int start,int mid,int end){
        int i = start,j = mid+1,k=start;
        while(i!=mid+1&&j!=end+1){
            if(arr[i]>arr[j]){
                temp[k++]=arr[j++];
            }else{
                temp[k++]=arr[i++];
            }
        }
        while(i!=mid+1){
            temp[k++]=arr[i++];
        }
        while (j!=end+1){
            temp[k++]=arr[j++];
        }
        for (int n = start; n <=end ; n++) {
            arr[n]=temp[n];
        }
    }

    public static void mergeSort(int[] arr,int[] temp,int start,int end){

        if(start>=end){
            return;
        }

        int mid = (start+end)/2;
        mergeSort(arr,temp,start,end);
        mergeSort(arr,temp,mid+1,end);
        merge(arr,temp,start,mid,end);
    }

    public static void mergeSort(int[] arr){
        int[] temp = new int[arr.length];
        mergeSort(arr,temp,0,arr.length-1);
    }
}


