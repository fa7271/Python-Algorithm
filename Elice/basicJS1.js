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