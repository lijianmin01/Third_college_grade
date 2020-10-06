#include <iostream>
using namespace std;
typedef long long ll;

//代码预处理区
 
const int MAX = 1e5 + 7;
int n, info[MAX], tmp[MAX];
ll ans;
//全局变量区
 
void merge(int l, int mid, int r);
void merge_sort(int l, int r);
//函数预定义区
 
int main() {
    int t;
    cin>>t;
    while(t--){
        cin >> n;
        for (int i = 1; i <= n; i++) cin >> info[i];
        merge_sort(1, n);
        cout << ans << endl;
    }
    
    return 0;
}
void merge_sort(int l, int r) {
    if (l == r) return;
    int mid = l + r >> 1;
    merge_sort(l, mid);
    merge_sort(mid + 1, r);
    merge(l, mid, r);
}
void merge(int l, int mid, int r) {
    int x = l, y = mid + 1;//左右进行二路归并
    int pos = 1;//记录临时数组的最大位置
    while (x <= mid && y <= r) {
        if (info[x] > info[y]) {
            tmp[pos++] = info[y++];
            ans += mid - x + 1;
        }
               //如果前面的数大于后面的，说明我们在临时数组要保存后面的
                //既然是要保存后面的，说明后面那个数要跳跃mid - x + 1个到前面来
                else {
            tmp[pos++] = info[x++];
        }
    }
    while (x <= mid) tmp[pos++] = info[x++];
    while (y <= r) tmp[pos++] = info[y++];
    for (int i = r; i >= l; i--) info[i] = tmp[--pos];
}