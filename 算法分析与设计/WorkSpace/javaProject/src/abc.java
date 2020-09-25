import java.lang.reflect.Array;
import java.util.Arrays;

public class abc {
    public static void main(String[] args) {
        int[] arr={3,0,10,2,9,1};
        selectionSort1(arr);
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

}


