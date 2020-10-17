import java.lang.reflect.Array;
import java.util.Arrays;

public class 快排 {
    public static void main(String[] args){
        int[] arr={5,1,7,8,3,2,9,4};
        System.out.println("原数组："+Arrays.toString(arr));
        quitSort(arr);
        System.out.println("排序之后的数组："+Arrays.toString(arr));

    }


    // 快排包装
    public static void quitSort(int[] arr){
        quitSort(arr,0,arr.length-1);
    }
    //快速排序，可以将arr数组，将left~right进行排序
    public static void quitSort(int arr[],int left,int right){
        //终止条件
        if(left>=right){
            return;
        }
        int mid = partition(arr,left,right);
        quitSort(arr,0,mid-1);
        quitSort(arr,mid+1,right);

    }
    public static int partition(int[] arr,int low,int high){
        while(low<high){
            while (low<high && arr[low]<arr[high]){
                high--;
            }
            if(low<high){
                int temp = arr[low];
                arr[low] = arr[high];
                arr[high] = temp;
                low++;
            }
            while(low<high && arr[low]<=arr[high]){
                low++;
            }
            if(low<high){
                int temp = arr[low];
                arr[low] = arr[high];
                arr[high] = temp;
                high--;
            }
        }
        return low;
    }

}


/*
//
//    * 给定一个数组arr,和一个数num，请把小于num的数放在数组的左边，等于num的数放在数组的中间，大于num的数放在数组的右边
//    * 快排的优化
//    *
public static void partition2(int[] arr,int pivot){
    int low=0,high=arr.length-1;
    //栅栏
    int left=-1,right=arr.length;
    while (low<=high){
        if(arr[low]<pivot){
            left++;
            swap(arr,low,left);
            low++;
        }else if(arr[low]>pivot){
            right--;
            swap(arr,low,right);
            high--;
        }else{
            low++;
        }
    }
}

    private static void swap(int[] arr, int low, int left) {
        int t = arr[low];
        arr[low]=arr[left];
        arr[left]=t;
    }
* */
