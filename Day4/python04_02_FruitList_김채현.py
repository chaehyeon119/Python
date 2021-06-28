'''
5/3 목요일 실습예제02
<조건>
01. 10이상의 숫자를 입력 받는다.
02. 10이하의 숫자이면,
^  10이상의 숫자 확인 하세요.

03. 10이상이라면,
-3 으로 나눠 떨어진 수 : Apple
-4 으로 나눠 떨어진 수 : Melon
-5 으로 나눠 떨어진 수 : Grape
-8 으로 나눠 떨어진 수 : StrawBerry 출력

'''

while True:
	n=int(input('10이상의 수를 입력해주세요.'))
	if n>=10:
		for n in range(1, n+1):
			if n%3==0:
				print('Apple')
			if n%4==0:
				print('Melon')
			if n%5==0:
				print('Grape')
			if n%8==0:
				print('StrawBerry')
	elif n<10:
		print('10이상의 수를 확인 하세요.')





'''
A=0
M=0
S=0
G=0

while True:
	n=int(input(">>10이상의 수를 입력 하세요.[Exit : 0]"))
	for n in range(1,i+1):
		if n>=10:
			n%3n==0
			print('Apple')
			n%4n==0
			print('Melon')
			n%5n==0
			print('Grape')
			n%8n==0
			print('StrawBerry')
		else:
			print('^ 10이상의 숫자 확인 하세요.')
			print('==<< 15번 반복합니다. >>==')
'''
