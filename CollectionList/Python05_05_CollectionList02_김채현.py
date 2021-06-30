#Python05_05_CollectionList02_김채현

a=[1,2,3,['a','b','c']]
print(a[0])    #1
print(a[-1]) #['a','b','c']
print(a[3]) #['a','b','c']
print('-'*15)

print(a[-1][0]) #a
print(a[-1][-1]) #c

a=[1,2,['a','b',['Life','is']]]
print(a[2][2][0]) #Life