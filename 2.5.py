price_list_products = [57.8, 46.51, 97, 79, 96, 35, 8, 1, 69]
print(id(price_list_products))
price_list_products_format=[]

for i in price_list_products:

    if type(price_list_products[price_list_products.index(i)]) == float:
        meaning = str(price_list_products[price_list_products.index(i)])
        r, kk=meaning.split('.')
        r=int(r)
        kk=int(kk)
        if r <=9:
            if kk <= 9:
                price_list_products_format.append(f'«0{r} руб 0{kk} коп»')
            else:
                price_list_products_format.append(f'«0{r} руб {kk} коп»')
        else:
            if kk<=9:

                price_list_products_format.append(f'«{r} руб 0{kk} коп»')

            else:
                price_list_products_format.append (f'«{r} руб {kk} коп»')

    elif type(price_list_products[price_list_products.index(i)]) == int:
        r = price_list_products[price_list_products.index(i)]
        kk = 00
        if r <= 9:

            price_list_products_format.append(f'«0{r} руб 0{kk} коп»')
        else:

            price_list_products_format.append(f'«{r} руб 0{kk} коп»')




price_list_products = [57.8, 46.51, 97, 79, 96, 35, 8, 1, 69]
print(price_list_products_format)
print(id(price_list_products))

price_list_products_format.sort()
print(price_list_products_format)
print(id(price_list_products))

price_list_products_format = price_list_products_format[::-1]
print(price_list_products_format)
print(id(price_list_products_format))

print('Вывести цены пяти самых дорогих товаров')
print(price_list_products_format[:5])