import java.util.InputMismatchException;
import java.util.Scanner;

public class test3 {

    public static void quickSort(int[]arr, int start, int end) {
        if(start>=end) {                                // 퀵정렬 알고리즘
            return;                                     // 원소 1개면 종료
        }
        int pivot = start;                                // 리스트 첫번째를 기준점으로 가짐
        int left = start+1;                             // 왼쪽값 설정
        int right=end;                                  // 우측값 설정
        while(left<=right) {
            while(left<=end&&arr[left]<=arr[pivot]) {
                left++;                                  // 큰 데이터 찾을 떄 까지 반복
            }
            while(right>start&&arr[right]>=arr[pivot]) {
                right--;                                 // 작은 데이터 찾을 떄 까지 반복
            }

            if(left>right) {                             // 찾는 값이 엇갈렸을때
                int temp = arr[pivot];
                arr[pivot] = arr[right];
                arr[right] = temp;
            }else {
                int temp = arr[left];
                arr[left]= arr[right];
                arr[right]=temp;
            }
        }
        quickSort(arr, start, right-1);             // 분할이후 왼쪽에서 정렬수행
        quickSort(arr, right+1,end);               // 분할이후 오른쪽에서 정렬 수행
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[10];
        int pivot = 0;

        for (int i = 0; i < arr.length; i++) {
            System.out.print("숫자 " + (i+1) + " : ");
            try{
                pivot = sc.nextInt();
                arr[i] = pivot;
            }catch(InputMismatchException e){
                System.out.println("[입력오류] : 숫자로 입력해주세요.");
                sc.next();
                i--;
                continue;
            }
        }
        quickSort(arr,0,arr.length-1);
        System.out.print("결과 : ");
        for (int i = 0; i < arr.length-1; i++) {
            System.out.print("" + arr[i] + ", ");
            if (i == 8 ){
                System.out.print(arr[9]);
            }
        }
    }
}
