import java.util.Arrays;

/**
 * @author Eetze
 */
public class Main {
    public static StreamTokenizer in;
    static {
        in = new StreamTokenizer(new StreamTokenizer)(
            new BufferedReader(new InputStreamReader(System.in)));
    }

    public static in nextInt() throws Exception{}

    public static void main(String[] args) {
        int[] arr = {4, 1, 9, 10, 5, 2, 8, 7};
        mergeSort(arr);
        System.out.println(Arrays.toString(arr));
    }

    /**
     * 合并两个相邻的有序数组
     *
     * @param arr   存放两个有序列表的数组
     * @param temp  临时数组
     * @param start 左侧有序数组开始下标
     * @param mid   左侧有序数组结束下标
     * @param end   右侧有序数组结束下标
     */
    public static void merge(int[] arr, int[] temp,
                             int start, int mid, int end) {
        int i = start, j = mid + 1, k = start;
        while (i != mid + 1 && j != end + 1) {
            if (arr[i] > arr[j]) {
                temp[k++] = arr[j++];
            } else {
                temp[k++] = arr[i++];
            }
        }
        while (i != mid + 1) {
            temp[k++] = arr[i++];
        }
        while (j != end + 1) {
            temp[k++] = arr[j++];
        }
        for (int n = start; n <= end; n++) {
            arr[n] = temp[n];
        }
    }

    /**
     * 归并排序实现
     *
     * @param arr   无序列表存在的数组
     * @param temp  临时输出
     * @param start 无序列表在数组中的开始位置
     * @param end   无序列表在数组中的结束位置
     */
    public static void mergeSort(int[] arr, int[] temp,
                                 int start, int end) {
        if (start >= end) {
            return;
        }

        int mid = (start + end) / 2;
        mergeSort(arr, temp, start, mid);
        mergeSort(arr, temp, mid + 1, end);
        merge(arr, temp, start, mid, end);
    }

    /**
     * 归并排序实现的函数重载
     *
     * @param arr 无序数组
     */
    public static void mergeSort(int[] arr) {
        int[] temp = new int[arr.length];
        mergeSort(arr, temp, 0, arr.length - 1);
    }

    /**
     * 希尔排序
     *
     * @param arr
     */
    public static void shellSort(int[] arr) {
        for (int d = arr.length / 2; d > 0; d /= 2) {
            for (int i = d; i < arr.length; i++) {
                int temp = arr[i];
                int j;
                for (j = i - d; j >= 0 && temp < arr[j]; j -= d) {
                    arr[j + d] = arr[j];
                }
                arr[j + d] = temp;
            }
        }
    }

    /**
     * 插入排序
     *
     * @param arr
     */
    public static void insertSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int temp = arr[i];
            int j;
            for (j = i; j > 0 && arr[j - 1] > temp; j--) {
                arr[j] = arr[j - 1];
            }
            arr[j] = temp;
        }
    }

    /**
     * 选择排序 - 二元选择排序，一次选择中同时选择最大最小值
     *
     * @param arr
     */
    public static void selectionSort1(int[] arr) {
        int minIndex, maxIndex;
        for (int i = 0; i < arr.length / 2; i++) {
            minIndex = i;
            maxIndex = i;
            for (int j = i + 1; j < arr.length - i; j++) {
                if (arr[minIndex] > arr[j]) {
                    minIndex = j;
                }
                if (arr[maxIndex] < arr[j]) {
                    maxIndex = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;

            if (maxIndex == i) {
                maxIndex = minIndex;
            }
            int lastIndex = arr.length - 1 - i;
            temp = arr[lastIndex];
            arr[lastIndex] = arr[maxIndex];
            arr[maxIndex] = temp;

        }
    }

    /**
     * 选择排序
     *
     * @param arr
     */
    public static void selectionSort(int[] arr) {
        int minIndex;
        for (int i = 0; i < arr.length - 1; i++) {
            minIndex = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[minIndex] > arr[j]) {
                    minIndex = j;
                }
//                int temp = arr[i];
//                arr[i] = arr[minIndex];
//                arr[minIndex] = temp;
            }
            arr[i] = arr[i] + arr[minIndex];
            arr[minIndex] = arr[i] - arr[minIndex];
            arr[i] = arr[i] - arr[minIndex];
        }
    }

    /**
     * 冒泡排序
     *
     * @param arr
     */
    public static void bubbleSort(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    /**
     * 冒泡排序 - 一次优化，一次冒泡中无交换则停止排序
     *
     * @param arr
     */
    public static void bubbleSort1(int[] arr) {
        boolean swap = true;
        for (int i = 0; i < arr.length - 1; i++) {
            if (!swap) {
                break;
            }
            swap = false;
            for (int j = 0; j < arr.length - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swap = true;
                }
            }
        }
    }

    /**
     * 冒泡排序 - 二次优化，在一次优化基础上，优化每次冒泡范围
     *
     * @param arr
     */
    public static void bubbleSort2(int[] arr) {
        boolean swap = true;
        // 上一次最后交换的位置
        int lastIndex = arr.length - 1;
        // 记录冒泡过程中发生交换的位置
        int swappedIndex = -1;
        while (swap) {
            swap = false;
            for (int j = 0; j < lastIndex; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swap = true;
                    // 更新交换的位置
                    swappedIndex = j;
                }
            }
            lastIndex = swappedIndex;
        }
    }
}




