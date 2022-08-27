import java.io.BufferedReader;
import java.io.InputStreamReader;

import java.util.*;

public class test5 {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        List<Integer> res = new ArrayList<Integer>();
        List<Integer> sosu_list = new ArrayList<Integer>();      // sosu 담기위한 그릇

        int num = 0;
        int order = 1;      // 순서

        System.out.println("0을 입력하시면 입력이 종료 됩니다.");

        while(true){
            System.out.print("숫자 " + order + " : ");
            try {
                num = scan.nextInt();
                if(num == 0){
                    break;
                }

                for(Integer resNum :res){                       // 인핸즈드 포문
                    if(resNum == num){
                        System.out.println("[입력오류] : 이미 입력된 숫자 입니다.");
                        break;
                    }
                }
                res.add(num);
                order += 1;
            } catch (NumberFormatException ne) {
                System.out.println("[입력오류] : 숫자로 입력해주세요.");
                scan.next();
                continue;
            }
        }

        System.out.print("결과 : ");

        for (int i = 0; i < res.size(); i++) {
            int sosu = res.get(i);

            boolean sosu_check = true;      // 소수인경우 true, 아닌경우 false

            if (sosu == 1) {                //1은 소수가 아니라서 계속 진행한다
                continue;
            }

            if (res.get(i) == 0){           // 0 이면 출력 되길래 continue 시킴
                continue;
            }

            for (int j = 2; j <= Math.sqrt(sosu); j++) {        // 제곱근까지 나눠주면 됨
                if (sosu % j == 0) {
                    sosu_check = false;
                }
            }

            if (sosu_check) {               //sosu_check가 true이면 소수이다 count에 누적시켜준다
                sosu_list.add(res.get(i));
            }
        }

        Collections.sort(sosu_list);

        for(int i = 0; i < sosu_list.size()-1; i++){
            System.out.print("" +sosu_list.get(i) + ", ");
        }

        for(int i = sosu_list.size()-1; i < sosu_list.size(); i++){
            System.out.println(""+sosu_list.get(i));
        }
    }
}
