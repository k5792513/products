products = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')
	p = [] #7到9行可以簡化為：p = [name, price]
	p.append(name)
	p.append(price)
	products.append(p) #7到10行可以簡化為：products.append([name, price]) 
print(products)