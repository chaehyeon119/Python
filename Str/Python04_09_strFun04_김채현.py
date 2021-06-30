#python04_09_strFun04_김채현
##스페이스 없앨 때 사용

a=' hi '
print(a)
print(a.lstrip()+'Chk')
print(a.rstrip()+'Chk')
print(a.strip()+'Chk')
print('-'*15)


#문자열 바꾸기(replace)
a='Life is too short'
print(a)
cng=a.replace('Life','Your leg')
print(cng)
print('-'*15)

cng=a.replace('Life', 'Your LEG')
print(cng)