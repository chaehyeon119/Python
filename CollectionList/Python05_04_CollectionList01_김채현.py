#Python05_04_CollectionList01_김채현

'''
형식: 리스트명=[요소1,요소2,요소3,...]
'''


a=[]
b=[1,2,3]
c=['Life','is','too','short']
d=[1,2,'Life','is']
e=[1,2,['Life','is']]

#비어 있는 리스트는 a=list()로 생성할 수도 있다.

#리스트의 인덱싱과 슬라이싱
a=[1,2,3]
print(a[0])   #1
print(a[0]+a[2])  ## 4
print(a[-1]) #3
print('-'*15)