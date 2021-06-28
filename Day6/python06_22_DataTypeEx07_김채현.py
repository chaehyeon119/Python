#python06_22_DataTypeEx07_김채현
'''
다른 주소를 가리키도록 만들 수는 없을까?
'''
a=[1,2,3]
b=a[:] #[:]처음부터 끝까지 저장해주세요
a[1]=4
print(a,'\t',b)

from copy import copy
a=[1,2,3]
b=copy(a)
print(b)
print(id(a))
print(id(b))
