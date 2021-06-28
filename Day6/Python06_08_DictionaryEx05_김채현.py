#Python06_08_DictionaryEx05_김채현

#Value 리스트 만들기(values)
a={'name':'pey','phone':'01199933232','birth':'1118'}

print(a.values()) # dic_values(['pey', '0119993323', '1118'])

print('-'*15)

#Key, Value 쌍 얻기(items)
print(a.items()) #dict_items([('name', 'pey'), ('phone', '01199933232'), ('birth', '1118')])

print('-'*15)

#Key:Value 쌍 모두 지우기(clear)

a.clear()
print(a)