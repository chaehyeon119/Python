#python05_15_MemberStep02lns_김채현

menu = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
print('{0:=^40}'.format('메뉴선택'),'\n')
for i in range(len(menu)):
	print(menu[i], end=' ')
print('\n')
print('='*44)

print('\n')
while True:
	n=input('{0:^30}'.format('메뉴의 번호를 선택해주세요 :'))
		if n=='1':
			print('{0:^30}'.format('SignUp'))
			for n in range(0,len(itemList)):
		elif n==2:
			print('{0:^30}'.format('2. 로그인 Algorithm Chk'))
		elif n==3:
			print('{0:^30}'.format('3. 회원목록 Algorithm Chk'))
		elif n==9:
			print('\t', '메뉴종료')
			break
		else:
			print('메뉴의 번호를 선택해주세요.')
		