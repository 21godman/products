products = []
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
	p = [name, price]

	products.append(p) # 也可以不定義 p 直接把 list 寫到括號裡面
print(products)

# 存取二維清單
# print(products[0][0])

# 列出每個東西
for p in products:
	print(p[0], '的價格是', p[1])

# str 可以做 + 和 *，int 不可以
# 寫入一個csv檔
# 解決程式編碼問題(encoding)
with open('products.csv', 'w', encoding = 'utf-8') as f:
	# 加入欄位
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')