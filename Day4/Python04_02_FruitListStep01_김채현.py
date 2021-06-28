#Python05_02_FruitListSample01_김채현


answer=[]
fruitCnt=[]
while True:
	num=int(input(">>10이상의 수를 입력 하세요.[Exit : 0]"))
	if num>=10:
		print('==<< %d번 반복합니다.>>=='%num)
		for i in range(1, num+1):
			if i%3==0:
				answer.append('Apple')
			if i%4==0:
				answer.append('Melon')
			if i%5==0:
				answer.append('Grape')
			if i%8==0:
				answer.append('StrawBerry')
			fruitCnt+=answer
			if len(answer)==0:
				print('%d.' %i)
			else:
				print('%d.'%i,str(answer))
			answer=[]

		print('==<<Fruit COunter List>>==')
		print('Apple : %d회'%fruitCnt.count('Apple'))
		print('Melon : %d회'%fruitCnt.count('Melon'))
		print('Grape : %d회'%fruitCnt.count('Graple'))
		print('StrawBerry : %d회'%fruitCnt.count('StrawBerry'))
	elif num==0:
		print('종료')
	else:
		print('10이상의 수를 확인해주세요.')
		break