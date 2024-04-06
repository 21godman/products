# 檢查檔案是否存在
import os # operating system

products = []
if os.path.isfile('products.csv'):
	print('YA! 找到檔案了!')
	# 讀取檔案
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			# 跳過 header
			if '商品,價格' in line: 
				continue	# 跳過此次迴圈，繼續執行下一個迴圈(break是跳出迴圈)
			# 先除掉換行符號(\n)，再用逗點做分割, 分別儲存在 name 和 price
			# split 完會變清單 list
			name, price = line.strip().split(',')	
			products.append([name, price])
	print(products)
else:
	print('找不到檔案...')

# 輸入新的清單內容
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')

	# 建立二維清單
	# p = []
	# p.append(name)
	# p.append(price)

	# 簡易寫法
	# p = [name, price]
	# products.append(p)

	#更簡易寫法
	products.append([name, price])
print(products)

# 存取二維清單
# print(products[0][0])

# 列出每個東西
for p in products:
	print(p[0], '的價格是', p[1])

# 寫入檔案
# str 可以做 + 和 *，int 不可以
# 解決程式編碼問題(encoding)
with open('products.csv', 'w', encoding = 'utf-8') as f:
	# 加入欄位
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')