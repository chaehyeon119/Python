menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
menuChk = ['1','2','3','4','9']
itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

#Data Setting -----------------------------------
dic = {} #dic에 itemList, MenuList 같이 넣기 / 초기화

for i in range(len(idList)):
	dic[idList[i]] = scoreList[i]
#Data Setting -----------------------------------

deleteIDList = []
idx = 0;

print('-'*80)
print('학생관리시스템v02')
print('-'*80)
for i in range(len(menu)):
	print(menu[i],end=' ')
print()
print('-'*80)

while True:
	n = int(input('번호 입력:'))
	if n == 9:
		print(menu[4])
		break
	elif n <= 4 and n >= 1:
		print('%s Algorithm Chk'%menu[n-1])
		# Menu 3 start------------------------------------------------------------------
		if n == 3:
			print()
			print('학생목록')
			print()
			for i in range(len(MenuList)):
				print(MenuList[i],end='\t')
			print()
			print('-'*65)
			''' 염충재 old version
			dickeyList = list(dic.keys()) #dic에 있는 key값을 리스트로 넣기
			dicvalueList = list(dic.values()) #dic에 있는 value값을 리스트로 넣기
			for k in range(len(dic)):
				print('%s  %s  %s  %s'%('{0:<6}'.format(dickeyList[k]),'{0:>4}'.format(dicvalueList[k][0]),'{0:>5}'.format(dicvalueList[k][1]),'{0:>6}'.format(dicvalueList[k][2])))
			'''
			# flash young version
			for keyname in dic.keys(): #dic의 key들을 keyname에 넣기
				print(keyname,'\t',dic[keyname][0],'\t',dic[keyname][1],'\t',dic[keyname][2])
			# Menu 3 end--------------------------------------------------------------------------------------------------------------------------------------------------------------------	
	else:
		print('Again check the menu!')