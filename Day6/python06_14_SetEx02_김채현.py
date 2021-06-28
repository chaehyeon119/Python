#python06_14_SetEx02_김채현
#교집합, 합집합, 차집합을 구할 때

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

#1. 교집합 동일한 결과 2가지 방법
inter1=s1&s2
inter2=s1.intersection(s2)
print(inter1) #{4,5,6}
print(inter2) #{4,5,6}

print('-'*15)
#합집합 동일한 결과 2가지 방법
vUnion1=s1|s2
vUnion2=s1.union(s2)
print(vUnion1) #{1,2,3,4,5,6,7,8,9}
print(vUnion2) #{1,2,3,4,5,6,7,8,9}

print('-'*15)

#차집합 동일한 결과 2가지 방법
differ1=s1-s2
differ2=s2-s1

differ3=s1.difference(s2)
differ4=s2.difference(s1)

print(differ1) #{1,2,3}
print(differ2) #{8,9,7}
print(differ3) #{1,2,3}
print(differ4) #{8,9,7}