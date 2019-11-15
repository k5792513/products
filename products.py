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

for p in products:
	print(p[0], '的價格是： ', p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')