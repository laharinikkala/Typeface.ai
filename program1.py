n  = int(input())
flag = 0
if n<0:
    flag = 1
n = abs(n)
res = ""
while n>=3:
    res+=str(n%3)
    n = n//3
res = res[::-1]
res =  str(n) +res
if flag:
    print("-"+res)
else:
    print(res)