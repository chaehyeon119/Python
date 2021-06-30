#Python06_09_DictionaryEx06_김채현

#Key로 Value 얻기(get)

a={'name':'pey', 'phone':'0119993323', 'birth':'1118'}
print(a.get('name')) #pey
print('-'*15)

'''
이름값으로 가져 올 수 있고 get으로도 가지고 올 수 있는데
없는 값을 가져오는 경우 get은 none으로 뜨고 이름값으로 가져오면
에러가 뜬다
'''

print(a.get('nokey'))  #NONE
#print(a['nokey']) ##에러 뜸

print('-'*15)

