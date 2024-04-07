import os # operating system

# 讀取檔案
def read_file(filename):
	with open(filename, 'r', encoding = 'utf-8') as f:
		products = []
		for line in f:
			# 跳過 header
			if '商品,價格' in line: 
				continue	# 跳過此次迴圈，繼續執行下一個迴圈(break是跳出迴圈)
			# 先除掉換行符號(\n)，再用逗點做分割, 分別儲存在 name 和 price
			# split 完會變清單 list
			name, price = line.strip().split(',')	
			products.append([name, price])
		return products

# 輸入清單內容
def user_input(products):
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
	return products

# 列出每個東西
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f: # 解決程式編碼問題(encoding)
		# 加入欄位
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n') # str 可以做 + 和 *，int 不可以


def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # 檢查檔案是否存在
		print('YA! 找到檔案了!')
		products = read_file(filename)
	else:
		print('找不到檔案...')

	products = user_input(products)
	print_products(products)
	write_file(filename, products)

main()