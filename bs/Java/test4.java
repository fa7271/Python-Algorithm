import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

public class test4 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        List<Integer> res = new ArrayList<Integer>();

        int num = 0;
        int order = 1;      // 순서
        System.out.println("0을 입력하시면 입력이 종료 됩니다.");
            while(true){
                System.out.print("숫자 " + order + " : ");
                try {
                    num = scan.nextInt();
                    res.add(num);
                    order += 1;

                } catch (InputMismatchException e) {
                    System.out.println("[입력오류] : 숫자로 입력해주세요.");
                    scan.next();
                    continue;
                }
                if(num == 0){
                    break;
                }
            }
        System.out.print("결과 : ");
        for (int i = 0; i <res.size() -2 ; i++) {
            System.out.print("" +res.get(i) + ", ");
        }
        for ( int i = res.size()-1 ; i < res.size(); i++){
            System.out.println(""+res.get(i-1));
        }
    }
}