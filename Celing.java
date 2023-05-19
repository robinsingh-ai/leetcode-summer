public class Celing {

    static int binarySearch(int []arr, int target){
        int start = 0;
        int end = arr.length-1;

        while(start<=end){
            int m = start+(end-start)/2;

            if (target<=arr[m]){
                end = m-1;
            }
            else if (target>arr[m]){
                start = m+1;
            }
            else{
                return m;
            };

        };

        return start;

    };
    public static void main(String[] args) {
        int [] arr = {2,5,8,10,12,18,19,20};
        int target = 15;

        int ans = binarySearch(arr, target);
        System.out.println(arr[ans]);
    }
}
