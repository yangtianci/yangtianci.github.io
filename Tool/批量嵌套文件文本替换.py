
import os

path="/Users/yangtiansi/Desktop/SourceTree/保险应用/HengtianOverseas/Modules"

count = 0

for root,dirs,files in os.walk(path):

	for name in files:

	# print name
		

		if name.endswith(".h"):

			print (root,dirs,name)

			count = count+1

			filename=root+"/"+name

			# 使用 open() 函数以只读模式打开我们的文本文件
			with open(filename, 'r',encoding='UTF-8') as file:
    			# 使用 read() 函数读取文件内容并将它们存储在一个新变量中
				data = file.read()
 
    			# 使用 replace() 函数搜索和替换文本
				data = data.replace("北京恒天明泽基销售有限公司", "青岛恒天睿信家族办公室有限公司")
 
			# 以只写模式打开我们的文本文件以写入替换的内容
			with open(filename, 'w',encoding='UTF-8') as file:
    			# 在我们的文本文件中写入替换的数据
				file.write(data)
# 打印文本已替换
			# print("文本已替换")
			

print(count)
