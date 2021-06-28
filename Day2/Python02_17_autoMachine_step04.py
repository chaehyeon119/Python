''' 1 ~ 6번까지
해당 index 값 출력'''
'''
홍익대학교 과일 판매머신 V03
1. orange	: 1000원
2. strawberry : 2500원
3. peach	: 1500원
4. mango	: 2000원
5. grape	: 2000원
6. 종료
'''
print("홍익대학교 과일 판매머신 V03")
menu = ["오렌지", "딸기", "복숭아", "망고", "포도", "종료"]
price = [1000, 2500, 1500, 2000, 2000]

for n in range(0, 5):
	print(n + 1, menu[n], price[n],"원")


while True:
	n = int(input("번호를 입력하세요."))
	
	if n in range(1, 7):
		print(menu[n - 1],"은/는", price[n - 1], "원입니다.")
	else:
		print("1에서 6번을 입력해주세요.")


	'''if n == 1:
		print(menu[n - 1],"은/는", price[n - 1], "원입니다.")
	elif n == 2:
		print(menu[n - 1],"은/는", price[n - 1], "원입니다.")
	elif n == 3:
		print(menu[n - 1],"은/는", price[n - 1], "원입니다.")
	elif n == 4:
		print(menu[n - 1],"은/는", price[n - 1], "원입니다.")
	elif n == 5:
		print(menu[n - 1],"은/는", price[n - 1], "원입니다.")
	elif n == 6:
		break
'''

