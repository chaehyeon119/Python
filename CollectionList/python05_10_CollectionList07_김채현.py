#python05_10_CollectionList07_김채현

a=['a','c','b']
a.reverse()
print(a) #['b', 'c', 'a']
print('-'*15)

#위치 변환(index)
a=['a','c','b']
print(a.index('b'))   #답: 2
#없는 애를 찾아주세요 하면 index는 에러/find는 찾아주긴 함
print('-'*15)

a=[1,2,3]
a.insert(0,4)  #[4,1,2,3]
print(a)

a.insert(3,5)  #[4,1,2,5,3]
print(a)

print('-'*15)
