#python06_18_DataTypeEx03_김채현
a=3
b=3
print('a is b:',a is b)
print('a == b', a==b)
print(id(a))
print(id(b))


'''
객체를 비교해주는게 'is'. id(a)의 값이
id(b)의 값과 동일함을 확인할 수 있다.
즉, a가 가리키는 대상과 b가 가리키는 대상이 동일하다는 것을
알 수 있다. 동일한 객체를 가리키고 있는지에 대해서
판단하는 파이썬 명령어 is를 다음과 같이 실행해도
역시 참(True)을 돌려준다.
'''
