#python05_09_CollectionList06_김채현

a=[1,2,3]
a.append(4)
print(a) #[1,2,3,4]

a.append([5,6])  # [1,2,3,4,[5,6]]
print(a)
print('-'*15)

#리스트 정렬(sort)
a=[1,4,3,2]
a.sort()
print(a)   #[1,2,3,4]

a=['a','c','b']
a.sort()    #['a', 'b', 'c']
print(a)
print('-'*15)