def solution(polynomial):
    res = polynomial.replace(" ","").split("+")
    num ="0"
    strr = "0"
    if "".join(res).isnumeric():
        return eval(polynomial)

    for i in res:
        if i.isnumeric():
            num = str(int(num)+int(i))
        else:
            if i == "x" and len(i) == 1:
                strr = str(int(strr) + 1)
            else:
                strr = str(int(strr) + int(i[:-1]))
    if num =="0" and strr =="0":
        return "0"
    if num == "0":
        return str(strr) +"x"
    elif strr == 0:
        return strr
    elif strr == "1":
        return "x" " + "+ num
    else:
        return str(strr) +"x"+" " + "+" + " " + num

def solution(polynomial):
    x, num = 0, 0
    polynomial = polynomial.split(" + ")
    for i in polynomial:
        if i.isnumeric():
            num += int(i)
        else:
            if len(i) == 1:
                x += 1
            else:
                x += int(i[:-1])
    if x == "0" and num == "0":
        return "0"
    if x == "0":
        return num
    if x == "1":
        x = ""
    if num == "0":
        return x + "x"
    return x + "x + " + num

# print(solution(	"x + x + x"))
# print(solution(	"3x + 73x + x"))
# print(solution("1 + 2 + 3 + 4"))
print(solution("5x + 12 + 72x"))
# print(solution("72x"))
# print(solution("72x+200"))
# print(solution("x + 200"))
# print(solution("7 + 1 + 2"))