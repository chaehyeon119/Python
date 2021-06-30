#python04_11_strFunExQueryString_김채현

## https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=python

URL="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=python"
a=(URL.split('?'))
b=(a[1].split('&'))
print(b[0:4],'\n')
print(b[1],'\n')
print(b[2],'\n')
print(b[3],'\n')
print(b[4],'\n')
print("QueryString 개수 :", URL.count('&')) 

