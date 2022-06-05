import java.util.InputMismatchException;
import java.util.Scanner;

public class test2 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int sum = 0, num = 0;
        for (int i = 1; i < 11; i++) {
            System.out.print("숫자 "+i+" : ");
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