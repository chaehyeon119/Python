#Python05_06_CollectionList03_김채현
#리스트의 슬라이싱
a=[1,2,3,4,5]
print(a[0:2])
print(a[:2])
print(a[2:])

print('-'*15)

#중첩된 리스트에서 슬라이싱하기

a=[1,2,3,['a','b','c'],4,5]  # [3,['a','b','c'],4]
print(a[2:5])
print(a[3][:2])

print('-'*15)