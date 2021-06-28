#Python02_15_AutoMachine_step02_김채현

menu=['오렌지','딸기','복숭아','포도','종료']
money=[1000,2500,1500,2000,2000,]
print("*******홍익대학교 과일 판매머신 V02*******")
for i in range(len(menu)):
    print(i+1,"번", menu[i],money[i],"원")
print("6,종료")
print("============================")

while True:
	n=input("구매번호를 입력하세요.(1~6):")
	n=int(n)
	if n==1:
		print(menu[n-1], "는", money[n-1], "원입니다!")
		print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<")