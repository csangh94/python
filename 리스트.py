# 입력을 받아서 리스트에 넣어봅시다.

data = []
for i in range(0,3):
    data.append(input("입력 >>"))
print("-----------------------------")

sum=0
for i in data:
    # print(i)
    sum=sum+int(i)
    if int(i) % 2 == 0:
        print("짝수 >>",i)
    elif int(i) % 2 != 0:
        print("X")

print("-----------------------------")

for i in range(0,3):
    print(data[i],end=" ")
print("\n-----------------------------")
print("총 합:",sum)
