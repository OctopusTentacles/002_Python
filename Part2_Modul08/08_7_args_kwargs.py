# подсчет суммы налога

def print_tax_document(tax, *args): # *-неизвестное количество
    price_sum = 0
    for i in args:
        price_sum = price_sum + i * tax / 100
    print('Сумма налога: ', price_sum)



my_tax = int(input('Величина налога: '))
print_tax_document(my_tax, 1000, 950, 880, 920, 990,    # налог и цены на товары
                   year=1997, 
                   doc_type='Report', 
                   operation_id=1110034)            # именнованные аргументы 