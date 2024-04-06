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