console.log(10 == 20)

if (조건) {
    명령어; // 조건이 참이면 코드가 실행
    if(조건){
        명령어 // 이중 이프문
    }
}
else if(조건){
    명령어; //여러개 조건일때 실행
} else {
    명령어; // 조건이 false 면 else 실행
}

반복분

for(초기변수값;조건;증감표시){
    수행명령
}
for (var i = 0; i < 10; i++) {
    console.log(i);
}

while (조건) {
    수행명령
}

do ~ while 문
do{
    명령
} while (조건){
    명령
}

주사위 게임
var dice = Math.floor(Math.random() * 6) +1;
// math.random 은 0 에서 1사이 임의 숫자 출력

소수 찾기
function prime(n){
    var sosu = 2;
    while (n > sosu){
        if(n % sosu ===0){
            return false;
        }else {
            sosu ++;
        }
    }return true;
}

믄자열 거꾸로 출력하기

function reverse(str) {
    var reverseStr = '';
    for (var i = str.length - 1; i >= 0; i--) { // 반대로 하나씩 내려옴
        reverseStr = reverseStr + str.charAt(i); //charat 란 특정 인덱스에 위치하는 유니코드 단일 문자를 반환
    }return reverseStr
}
console.log(reverse('hello'))
