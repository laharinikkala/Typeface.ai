invalid = ['3','4','7']

def is_valid(n):
    for i in str(n):
        if i in invalid:
            return False
    return True

num = int(input())

if num > 0:
    cnt = 0
    temp = 1

    while(cnt != num):
        if is_valid(temp):
            cnt += 1
        temp += 1

    print(temp-1)
