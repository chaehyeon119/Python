#python05_11_CollectionList08_김채현
#리스트 요소 제거(remove)_첫 번째 3만 제거

a=[1,2,3,1,2,3]
result01=a.remove(3)
print(result01)  #none
print(a)  #[1,2,1,2,3]

print('-'*15)

#pop은 뒤에서부터 한 개 제거
a=[1,2,3]
result2=a.pop()
print(result2) #3
print(a) #[1,2]
print('-'*15)