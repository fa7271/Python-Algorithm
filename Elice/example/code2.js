
// 구구단
// for (var i = 2; i<10; i++){
//     for (var j = 1; j < 10; j++) {
//         console.log(i +" x "+ j + " = " + i * j)
//     }
// }

function solution(num) {
    var answer = [];

    for(var i=2; i<num; i++) {
        if(num % i == 0) {
            answer.push(i);
        }
    }
    var res = [];
    for (var i = 0; i <answer.length; i++) {
        if (answer[i] == 2) {
            res.push(2 + "의 배수입니다.");
        }else if( answer[i] == 3){
            res.push(3 + "의 배수입니다.");
        }else if( answer[i] == 5){
            res.push(5 + "의 배수입니다.");
        }else if( answer[i] == 7){
            res.push(7 + "의 배수입니다.");
        }
    }
    var arr = res.join("\n");
    console.log(arr);
    return arr;
}



solution(21);