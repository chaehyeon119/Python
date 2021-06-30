#Python06_11_StudentMS_Step01_김채현

menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
menuChk = ['1','2','3','4','9']

print('-'*80)

print('학생관리시스템v01')

print('-'*80)
print('%s %s %s %s %15s'%(menu[0],menu[1],menu[2],menu[3],menu[4]))
print('-'*80)
while True:
	n=int(input('번호 입력:'))

'''

itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

dic = {}
deleteIDList = []
idx = 0;
'''