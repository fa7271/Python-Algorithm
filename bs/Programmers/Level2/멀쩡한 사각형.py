def gcd(x, h):
    max_xy = max(x, h)
    min_xy = min(x, h)
    while h > 0:
        x, h = h, x % h
    return max(x,h)
def solution(w,h):
    if w == h :
        return (w * h) - w
    if w <=1 or h <= 1:
        return 0
    else:
        return (w * h) - ( (w+h) - (gcd(w,h)))

print(solution(8, 12))



