#Python03_21_LenChk01_김채현

list01=[70,60,55,75,95,90,80,80,85,100]
print(len(list01))
sum=0
for n in list01:
	sum=sum+n

##소수점이하 2자리 확인
print("합계",sum)
print("평균",sum/len(list01))