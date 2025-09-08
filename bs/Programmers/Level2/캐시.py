
def solution(cacheSize, cities):
    # dic = { x: 0 for x in range(len(cities))}
    cache = []
    res = 0
    for i in cities:
        i = i.lower()
        if cacheSize:
            if not i in cache:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(i)
                res += 5
            else:
                cache.pop(cache.index(i))
                cache.append(i)
                res += 1
        else :
            res += 5
    return res

print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
