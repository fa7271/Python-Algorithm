def solution(phone_book):
    phone_book.sort()
    for i in range(1,len(phone_book)):
        if phone_book[i-1] == phone_book[i][:len(phone_book[i-1])]:
            return False
    return True
print(solution(["119", "97674223", "1195524421"]))
print(solution(["12","123","1235","567","88"]))