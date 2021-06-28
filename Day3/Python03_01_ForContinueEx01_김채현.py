#python03_02_AddOddEven_김채현

#1~10까지의 합 출력
add=0
for i in range(1,11):
	add=add+i

print("1-10까지의 합", add)

#1~10까지의 홀수 합 출력
odd=0
for i in range(1,11):
    odd=odd+i
print("1~10까지의 홀수합",odd)

#1~10까지의 짝수 출력
even=0
for i in range(0,11,2):
	even=even+i
print("1~10까지의 짝수합",even)