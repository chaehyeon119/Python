#1] 홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해보자.
# 과목 점수 국어 80 영어 75 수학 55

a=80
b=75
c=55
print((a+b+c)/3)

grade=(80,75,55)
average=sum(grade)/len(grade)
print(average)
print()

#2] 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해서 말해보자
while True:
	n=int(input('숫자입력'))
	if n%2==0:
		print('짝수입니다.')
		break
	else:
		print('홀수입니다.')
		break
print()

#3] 홍길동 씨의 주민등록번호는 881120-1068235이다. 홍길동 씨의
#주민등록번호를 연원일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해보자.

a='881120-1068234'
yyyymmdd=a[:6]
n=a[7:]
print(yyyymmdd)
print(n)
print()

#4] 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 1,3이면 남자 2,4면 여자 판별
b=(a.split('-'))

#5] 다음과 같은 문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로
#바꿔서 출력해보자

d='a:b:c:d'
print(d)
cng=d.replace(':','#')
print()
#6] [1,3,5,4,2] 리스트를 [5,4,3,2,1]로 만들어보자.

f=[1,3,5,4,2]
f.sort()
f.reverse()
print(f)

#7] ['Life', 'is', 'too', 'short']리스트를 Life is too short 문자열로
#만들어 출력해보자. *join 함수 사용

x=['Life', 'is', 'too', 'short']
result=' '.join(x)

#8] (1,2,3)튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해보자.
#튜플 더하기
t1=(1,2,3)
#t=t+(,4)
print(t) 

#9] 다음과 같은 딕셔너리 a가 있다.
