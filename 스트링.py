str = '가나다라마바사'

# 인덱싱과 슬라이싱이 된다

print(str[4:6])

str3 = '100:200:300:400:500'
a=str3.split(":")
int_map = map(int, a)
list_a= list(int_map)

sum=0
for x in list_a:
    sum = sum + x
print(sum)