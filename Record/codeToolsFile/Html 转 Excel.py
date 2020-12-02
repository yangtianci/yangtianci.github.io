#coding=utf-8 

from bs4 import BeautifulSoup 
import xlwt

path = '/Users/yangtianci/Desktop/埋点.html'


outerArr = [] 

with open(path, 'r') as f:
    Soup = BeautifulSoup(f.read(), 'lxml')
    
    big = Soup.find_all('tr') 

    for x in xrange(0,len(big)):
    	row = big[x] 
    	rowList = row.find_all('td')

    	rowArr = []

    	for Y in xrange(0,len(rowList)):
    		# print rowList[Y]
    		rowArr.append(rowList[Y].string) 
    		# print rowList[Y].string
    		# print '\n'
    		pass

    	outerArr.append(rowArr)

    	pass


# 创建 excel 并写入数据 

wb = xlwt.Workbook(encoding = 'utf-8')
ws = wb.add_sheet('iOS 埋点') 



for x in xrange(0,len(outerArr)):
	# print outerArr[x]
	# print '\n'
	innerArr = outerArr[x]
	for Y in xrange(0,len(innerArr)):

		ws.write(x,Y,innerArr[Y])

		pass

	pass

wb.save('/Users/yangtianci/Desktop/iOSTest埋点.xls')






