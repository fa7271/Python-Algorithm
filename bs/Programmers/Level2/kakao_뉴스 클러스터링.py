import re


def solution(str1, str2):
    str1 = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]','', str1).lower()
    str2 = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]','', str2).lower()
    lst1=[]
    lst2=[]
    for x,y in zip(str1,str2):
        lst1.append(x)
        lst2.append(y)
    result1 =[]
    result2 =[]
    for i in range(len(str1)-1):
        result1.append(lst1[i:i+2])
    for i in range(len(str2)-1):
        result2.append(lst2[i:i+2])
    print(set(result1) & set(result2))
print(solution("FRANCE", "french+"))