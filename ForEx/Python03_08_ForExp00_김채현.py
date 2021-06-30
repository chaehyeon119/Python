#Python03_08_ForExp00_김채현

a=[1,2,3,4]
result=[]
for num in a:
	result.append(num*3)
	
print(result)

print("=" *50)


result=[num*3 for num in a]
print(result)

#Python03_06_GuGuDanX03
a=[1,2,3,4]
result=[a]
for num in a:
	result.append(num*3)
print(result)

print('='*50)




a=[1,2,3,4]
result=[a]
for num in a:
	result.append(num*3)
	print(result)
