def call_10_times(func):
    for i in range(10):
        func(i)
call_10_times(lambda number: print("hi",number))


a = list(range(10))
lst = [i for i in range(10)] # 용량을 차지한다 >> 메모리를 차지한다.
print(map(lambda x: x*x , a)) #  map, filter 함수 제너레이터 함수라 내부의 데이터가 실제 메모리에 용량을 차지안함
print(a,lst, sep="\n")