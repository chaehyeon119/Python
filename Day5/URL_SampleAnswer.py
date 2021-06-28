

#URL_SampleAnswer_충재

s = input('주소를 입력하세요.:')

list1 = s.split('?')
list2 = list1[1].split('&')

print('\nURL: %s\n'%list1[0])
for i in range(len(list2)):
	print('  %s'%list2[i-1])

print('\nQuertString 개수: %d개'%len(list2))