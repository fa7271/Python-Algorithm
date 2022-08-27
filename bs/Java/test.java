import java.util.InputMismatchException;
import java.util.Scanner;

public class test {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int sum = 0, num = 0;
        for (int i = 0; i < 2; i++) {
            if(i==0) {
                System.out.print("첫번쨰 숫자를 입력해주세요 :");
            }
            if(i==1){
                System.out.print("두번째 숫자를 입력해주세요 :");

            }
            try {
                num = scan.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("[입력오류] : 숫자로 입력해주세요.");
                scan.next(); // 기존에 있던거 초기화
                i--;
                continue;
            }
            sum += num;
        }
        System.out.println("결과 :" + sum);
        scan.close();
    }
}