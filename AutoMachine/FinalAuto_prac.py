#Python02_20_AutoMachine_step05Finish_김채현

menu=['오렌지','딸기','복숭아','망고','포도']
money=[1000,2500,1500,2000,2000]
print("*******홍익대학교 과일 판매머신 V02*******")
for i in range(0,5):
    print(i+1,"번", menu[i],money[i],"원")
print("6,종료")
print('='*10)

while True:
	n=input("구매번호를 입력하세요.(1~6):")
	n=int(n)
	if n in range(1,6):
		print(menu[n-1], "는", money[n-1], "원입니다!")
		print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
		coin=int(input("코인을 투입하세요:"))
		print('='*10)
		print('선택한 과일: %s'%menu[n-1])
		print('받은 금액: %d원'%coin)
		print('==거스름돈==')
		change=coin-money[n-1]
		if coin>=money[n-1]:
			print('거스름돈은 %d원 입니다' %change)
		else:
			print('^금액 부족 확인.')

	elif n==6:
		print("종료")
		print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
		break
	else:
		print("번호 확인 바람")

	