#Python06_07_DictionaryEx04_김채현
'''
딕셔너리 관련 함수들
Key 리스트 만들기(Keys)
'''

a={'name':'pey','phone':'0119993323','birth':'1118'}
print(a.keys()) #dict_keys(['name','phone','birth'])


'''
dict_keys,dic_values, dic_items 등은 리스트로
변환하지 않더라도 기본적인 반복(iterate) 구문(예:for문)을
실행할 수 있다.
'''

for k in a.keys():
	print(k) #name
	         #phone
			 #birth
print('-'*15)

#dict_keys 객체를 리스트로 변환하려면 다음과 같이 하면 된다.
vList=list(a.keys())   
print(vList)	#['name','phone', 'birth']
print('-'*15)