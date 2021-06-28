#Python06_05_DicionaryEx02_김채현

'''
딕셔너리 쌍 추가하기
a[2]='b'와 같이 입력하면 딕셔너리 a에 Key와 Value가 각각
2와 'b'dls 2:'b'라는 딕셔너리 쌍이 추가
'''

a={1:'a'}
a[2]='b'
print(a) #{1:'a',2:'b'}

a['name']='pey'
print(a) #{1:'a', 2:'b', 'name':'pey'}
print('-'*15)

del a[1]
print(a) #{2:'b', 'name':'pey'}
print('-'*15)


