str1 = input()
str2 = input()
count = 0
for i in str1:
    if i == str2[-1]:
        count+=1
print(count)