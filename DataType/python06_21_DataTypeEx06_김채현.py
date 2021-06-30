#python06_21_DataTypeEx06_김채현

vI01=30
vI02=30

print('교환전 값:', vI01, vI02)
temp=vI01 #빈 병의 역할:temp
vI01=vI02
vI02=temp
print('교환후 값:', vI01, vI02)

a=3
b=5
print('교환전 값:',a,b)
a,b=b,a
print('교환후 값:',a,b)