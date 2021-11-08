print("continue문")

for i in range(11):
    if i%2==1:
        continue
    print(i)

print("\n\n break 문")
for i in range(11):
    if i%2==1:
        break
    print(i)


print("\n\n else 문 1")
for i in range(11):
    if i%2==1:
        continue
    print(i)
else:
    print("for문 종료")


print("\n\n else 문 2")
i=1
while i<=5:
    print(i)
    i+=1
else:
    print("완료")
